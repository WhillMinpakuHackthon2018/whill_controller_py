import math

class Measure:

    is_forward = True

    angle_left_rad_prev = 0
    angle_right_rad_prev = 0

    angle_left_rad = 0
    angle_right_rad = 0
    
    ## 回転(度)
    angle = 0

    ## 進行距離(cm)
    distanceX = 0 
    distanceY = 0

    def update(self, whill):
        angle_left_rad = self.__calc_rad_diff(self.angle_left_rad_prev, whill.left_motor['angle'])
        angle_right_rad = -1 * self.__calc_rad_diff(self.angle_right_rad_prev, whill.right_motor['angle'])

        #print(angle_left_rad, angle_right_rad)

        # if whill.time_diff_ms == 0.0:
        #     return
        dt = whill.time_diff_ms 
        #dt = 50.0

        left_angle_speed = angle_left_rad / (dt / 1000.0)
        right_angle_speed = angle_right_rad / (dt / 1000.0)

        left_speed = left_angle_speed * 0.270  
        right_speed = right_angle_speed * 0.270
        #print(left_speed, right_speed)

        speed = (left_speed + right_speed) / 2.0
        angle_speed = (left_speed - right_speed) / (2.0 * 0.1325)

        #print(angle_speed)

        self.distanceX += speed * (dt / 1000.0) * math.cos(self.angle + speed * (dt / 1000.0) / 2.0)
        self.distanceY += speed * (dt / 1000.0) * math.sin(self.angle + speed * (dt / 1000.0) / 2.0)

        #print(speed, angle_speed)

        # 右回転がマイナス
        self.angle += angle_speed * (dt / 1000.0)

        print(self.distanceX, self.distanceY, self.angle)

        self.angle_left_rad_prev = whill.left_motor['angle']
        self.angle_right_rad_prev = whill.right_motor['angle']

    def reset(self):
        self.distancemm = 0
        self.angle = 0

    def __calc_rad_diff(self, past, current):
        #print(past, current)
        diff = past - current
        if past * current < 0 and math.fabs(diff) > math.pi:  # Crossed +PI/-PI[rad] border
            diff = math.pi - math.fabs(past) + (math.pi-math.fabs(current))  # - to +
            if past > 0 and current < 0:  # Case of + to -
                diff = -1 * diff
        return diff

    def __calc_diff_angle(self, current_rad, prev_rad): 
        if self.is_forward:
            if prev_rad < current_rad:
                return current_rad - prev_rad
            else:
                return math.pi * 2.0 - prev_rad + current_rad
        else:
            if prev_rad > current_rad:
                return prev_rad - current_rad 
            else:
                return math.pi * 2.0 - current_rad + prev_rad