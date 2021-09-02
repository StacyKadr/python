from time import sleep
class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']
    count = 1

    def running(self, n):
        repeat=0
        while repeat <= n:
            for TrafficLight.count in range(1,4):
                print(f'{TrafficLight.__color[TrafficLight.count - 1]}')
                if TrafficLight.count ==1:
                    sleep(7)
                elif TrafficLight.count ==2:
                    sleep(2)
                elif TrafficLight.count == 3:
                    sleep(7)
                TrafficLight.count += 1
            repeat += 1

traffic_light = TrafficLight()
traffic_light.running(1)