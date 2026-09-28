class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stacky = []
        cars = sorted(zip(position, speed), reverse=True)
        for i, pos in enumerate(cars):
            time = (target-pos[0])/pos[1]
            if len(stacky) == 0:
                stacky.append(time)
            elif stacky[-1] < time:
                stacky.append(time)

        return len(stacky)





        