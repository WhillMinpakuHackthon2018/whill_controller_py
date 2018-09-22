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
    distancemm = 0 

    def update(self, whill):
        left_motor_angle_input = whill.left_motor['angle'] + math.pi
        right_motor_angle_input = whill.right_motor['angle'] + math.pi
        
        self.angle_left_rad = self.__calc_diff_angle(left_motor_angle_input, self.angle_left_rad_prev)
        self.angle_right_rad = self.__calc_diff_angle(right_motor_angle_input, self.angle_right_rad_prev)

        self.distancemm = self.angle_left_rad * 270 * math.pi
        #print(whill.left_motor['angle'])
        #print(self.distancemm)

        self.angle_left_rad_prev = left_motor_angle_input
        self.angle_right_rad_prev = right_motor_angle_input

    def reset(self):
        self.distancemm = 0
        self.angle = 0

    def __calc_diff_angle(self, current_rad, prev_rad): 
        if self.is_forward:
            if prev_rad < current_rad:
                return current_rad - prev_rad
            else:
                return math.pi * 2 - prev_rad + current_rad
        else:
            if prev_rad > current_rad:
                return prev_rad - current_rad 
            else:
                return math.pi * 2 - current_rad + prev_rad