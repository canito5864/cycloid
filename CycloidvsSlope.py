import pygame
import sys
from math import sin, cos
import numpy as np

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CycloidvsSlope")

# 색
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

r = 40  # 사이클로이드 곡선 반지름
x = []  # 사이클로이드 x 좌표 리스트
y = []  # 사이클로이드 y 좌표 리스트

for theta in np.linspace(0, np.pi, 1000): # 사이클로이드 곡선 좌표 생성
    x.append(50+r * (theta - sin(theta)))
    y.append(200 + r * (1 - cos(theta)))

# 경사면 관련 설정
slope_height = 80  # 경사면의 높이
slope_length = 125  # 경사면의 길이
slope_x1 = 600
slope_x2 = 600 + slope_length
slope_y1 = 190
slope_y2 = 190 + slope_height

# 공 관련 설정
ball_radius = 10
ball1_x = x[0]  # 초기 공의 x 좌표를 사이클로이드 시작 지점으로 설정
ball1_y = y[0] - ball_radius  # 초기 공의 y 좌표를 사이클로이드 시작 지점에서 위로 조금 올림
ball2_x = slope_x1  # 초기 공의 x 좌표를 경사면 시작 지점으로 설정
ball2_y = slope_y1 - ball_radius  # 초기 공의 y 좌표를 경사면 시작 지점에서 위로 조금 올림

time = 0
time_step = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    for i in range(1, len(x)):
        pygame.draw.line(screen, white, (x[i-1], y[i-1]), (x[i], y[i]), 4) # 사이클로이드 곡선 보여주기

    pygame.draw.line(screen, white, (slope_x1, slope_y1), (slope_x2, slope_y2), 4) #경사면 보여주기

    # Update the position of ball1 (the one following the cycloid curve)
    if time < len(x) - 1:
        time += time_step
        ball1_x = x[time]
        ball1_y = y[time] - ball_radius

    # Update the position of ball2 (the one on the slope)
    if ball2_x < slope_x2:  # Keep moving if ball2 is not at the end of the slope
        ball2_x += 0.1
        ball2_y += 0.1*0.64 # 경사면 위 공은 직접 좌표 설정
    else:
        pass

    pygame.draw.circle(screen, red, (int(ball1_x), int(ball1_y)), ball_radius)
    pygame.draw.circle(screen, blue, (int(ball2_x), int(ball2_y)), ball_radius)

    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()

