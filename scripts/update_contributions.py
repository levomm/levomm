#!/usr/bin/env python3
"""Build a real April-October contribution heatmap from GitHub GraphQL.

Only GitHub-reported contributions are used; never synthesize activity.
The default GITHUB_TOKEN can show public contributions. A read:user token in
CONTRIBUTIONS_TOKEN may additionally allow private contribution counts.
"""
import html
import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

LOGIN = "levomm"
FIRST = date(2026, 4, 1)
LAST = date(2026, 10, 31)
TARGET = Path("assets/activity-2026-gray.svg")
COLORS = {
    "NONE": "#c4c7c3",
    "FIRST_QUARTILE": "#a2a6a2",
    "SECOND_QUARTILE": "#808580",
    "THIRD_QUARTILE": "#585e59",
    "FOURTH_QUARTILE": "#282d29",
}
MONTHS = ["", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def retrieve_calendar():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GH_TOKEN or GITHUB_TOKEN is required. No fake data will be rendered.")

    # Use local Estonian date for the visible range, not runner UTC midnight.
    today = min(datetime.now(ZoneInfo("Europe/Tallinn")).date(), LAST)
    if today < FIRST:
        raise RuntimeError("Date range has not started")

    query = """
    query ProfileContributions($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays { date contributionCount contributionLevel }
            }
          }
        }
      }
    }
    """
    until = min(datetime.now(timezone.utc), datetime(2026, 10, 31, 23, 59, 59, tzinfo=timezone.utc))
    body = json.dumps({
        "query": query,
        "variables": {
            "login": LOGIN,
            "from": "2026-04-01T00:00:00Z",
            "to": until.isoformat().replace("+00:00", "Z"),
        },
    }).encode()
    req = Request(
        "https://api.github.com/graphql",
        data=body,
        method="POST",
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "levomm-profile-heatmap",
        },
    )
    try:
        with urlopen(req, timeout=30) as response:
            result = json.load(response)
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"GitHub contribution request failed: {exc}") from exc

    if result.get("errors"):
        raise RuntimeError("GitHub GraphQL returned errors: " + json.dumps(result["errors"]))
    user = (result.get("data") or {}).get("user") or {}
    calendar = ((user.get("contributionsCollection") or {}).get("contributionCalendar") or {})
    weeks = calendar.get("weeks")
    if not weeks:
        raise RuntimeError("GitHub GraphQL did not return a contribution calendar")

    days = {}
    for week in weeks:
        for day in week.get("contributionDays") or []:
            d = date.fromisoformat(day["date"])
            if FIRST <= d <= today:
                level = day["contributionLevel"]
                count = int(day["contributionCount"])
                if level not in COLORS or count < 0:
                    raise RuntimeError(f"Unrecognized contribution value for {d}")
                days[d] = (count, level)

    # No silent gaps. A partially started current day may be missing in UTC.
    cursor = FIRST
    while cursor < today:
        if cursor not in days:
            raise RuntimeError(f"GitHub omitted calendar data for {cursor}")
        cursor += timedelta(days=1)
    if today not in days:
        days[today] = (0, "NONE")
    return today, days


def build_svg(today, days):
    first_sunday = FIRST - timedelta(days=(FIRST.weekday() + 1) % 7)
    x_pitch, y_pitch, square, x0, y0 = 41, 36, 30, 77, 111
    total = sum(count for count, _ in days.values())
    result = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="420" viewBox="0 0 1400 420" role="img">',
        f'<title>GitHub activity for {LOGIN}: {FIRST} through {today} ({total} contributions)</title>',
        '<rect width="1400" height="420" rx="12" fill="#d7d8d5"/>',
        '<rect x="1.5" y="1.5" width="1397" height="417" rx="11" fill="none" stroke="#b8bdb5" stroke-width="2"/>',
        '<text x="60" y="45" font-family="monospace" font-weight="900" font-size="25" letter-spacing="2" fill="#1e2520">ACTIVITY.LOG</text>',
        f'<text x="1340" y="45" text-anchor="end" font-family="monospace" font-size="19" fill="#515b53">01 APR - {today.day:02d} {MONTHS[today.month]} 2026</text>',
        '<path d="M60 69H1340" stroke="#aeb4ad" stroke-width="2"/>',
    ]

    for month in range(4, 11):
        first_day = date(2026, month, 1)
        if first_day > today:
            break
        week = (first_day - first_sunday).days // 7
        x = x0 + week * x_pitch + 2
        result.append(
            f'<text x="{x}" y="100" font-family="monospace" font-size="21" fill="#525952">{MONTHS[month].title()}</text>'
        )

    for d in sorted(days):
        count, level = days[d]
        col = (d - first_sunday).days // 7
        row = (d.weekday() + 1) % 7
        x, y = x0 + col * x_pitch, y0 + row * y_pitch
        color = COLORS[level]
        label = html.escape(f"{d.isoformat()}: {count} contribution" + ("" if count == 1 else "s"))
        result.append(
            f'<rect x="{x}" y="{y}" width="{square}" height="{square}" rx="5" fill="{color}"><title>{label}</title></rect>'
        )

    result.append('<text x="930" y="398" font-family="monospace" font-size="18" fill="#545a53">Less</text>')
    for i, color in enumerate(COLORS.values()):
        result.append(f'<rect x="{1000 + 38 * i}" y="378" width="25" height="25" rx="4" fill="{color}"/>')
    result.append('<text x="1210" y="398" font-family="monospace" font-size="18" fill="#545a53">More</text>')
    result.append(
        f'<text x="60" y="399" font-family="monospace" font-size="16" fill="#555d56">'
        f'{total} public contributions | refreshed {today.isoformat()} | GitHub GraphQL</text>'
    )
    result.append('</svg>')
    return "\n".join(result) + "\n"


def main():
    today, days = retrieve_calendar()
    svg = build_svg(today, days)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != svg:
        TARGET.write_text(svg, encoding="utf-8")
        print(f"Wrote verified GitHub contributions {FIRST}..{today}: {len(days)} days.")
    else:
        print("Contribution graph already up-to-date.")


if __name__ == "__main__":
    main()
