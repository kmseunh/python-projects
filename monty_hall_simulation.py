import random


class MontyHallSimulation:
    def __init__(self):
        self.doors = ["goat", "goat", "car"]
        random.shuffle(self.doors)

    def simulate(self, switch=False):
        # 참가자가 문 선택
        player_choice = random.randint(0, 2)

        # 호스트가 열 문 선택
        remaining_doors = [
            idx for idx in range(3) if idx != player_choice and self.doors[idx] != "car"
        ]
        host_choice = random.choice(remaining_doors)

        # 참가자가 선택 변경
        if switch:
            remaining_doors = [
                idx for idx in range(3) if idx != player_choice and idx != host_choice
            ]
            player_choice = remaining_doors[0]

        # 결과 확인
        if self.doors[player_choice] == "car":
            return True  # 참가자가 이긴 경우
        else:
            return False  # 참가자가 진 경우


if __name__ == "__main__":
    num_simulations = 10000
    wins_stay = sum(MontyHallSimulation().simulate() for _ in range(num_simulations))
    wins_switch = sum(
        MontyHallSimulation().simulate(switch=True) for _ in range(num_simulations)
    )

    print("참가자가 선택을 바꾸는 경우의 승리 수:", wins_switch)
    print("참가자가 선택을 유지하는 경우의 승리 수:", wins_stay)
