import requests


def translate_status(status):
    """경기 상태를 번역합니다."""
    if status == "Pre-Game":
        return "경기 준비 중"
    elif status == "Scheduled":
        return "예정됨"
    else:
        return status


def beautify_output(game):
    """경기 정보  포맷팅"""
    return f"{game['away_team']} vs {game['home_team']} - {game['game_time']} - {game['game_status']}"


def get_mlb_games():
    """MLB API를 통해 이번 주의 경기 일정을 가져옴."""
    url = "https://statsapi.mlb.com/api/v1/schedule?sportId=1"
    response = requests.get(url)
    data = response.json()
    games = []
    for date in data["dates"]:
        for game in date["games"]:
            home_team = game["teams"]["home"]["team"]["name"]
            away_team = game["teams"]["away"]["team"]["name"]
            game_time = game["gameDate"].split("T")[0]
            game_status = translate_status(game["status"]["detailedState"])
            game_info = {
                "home_team": home_team,
                "away_team": away_team,
                "game_time": game_time,
                "game_status": game_status,
            }
            games.append(game_info)
    return games


def main():
    print("=== 이번 주 MLB 경기 일정 ===")
    games = get_mlb_games()
    for game in games:
        print(beautify_output(game))


if __name__ == "__main__":
    main()
