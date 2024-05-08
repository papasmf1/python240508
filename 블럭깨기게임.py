import pygame
import sys

# 게임 화면의 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 패들의 크기와 위치 설정
PADDLE_WIDTH = 400
PADDLE_HEIGHT = 20
PADDLE_Y = SCREEN_HEIGHT - 50

# 공의 크기와 초기 속도 설정
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# 블록의 크기와 초기 위치 설정
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 30
NUM_BLOCKS = 8
BLOCK_SPACING = 10

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 패들 생성
paddle = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) // 2, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 생성
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# 블록 생성
blocks = []
for i in range(NUM_BLOCKS):
    block_x = i * (BLOCK_WIDTH + BLOCK_SPACING) + BLOCK_SPACING
    block_y = BLOCK_SPACING * 2
    blocks.append(pygame.Rect(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT))

# 점수
score = 0

# 폰트 설정
font = pygame.font.Font(None, 36)

# 게임 루프
while True:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 게임 재시작
                paddle = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) // 2, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
                ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
                ball_dx = BALL_SPEED_X
                ball_dy = BALL_SPEED_Y
                blocks = [pygame.Rect((i * (BLOCK_WIDTH + BLOCK_SPACING) + BLOCK_SPACING, BLOCK_SPACING * 2, BLOCK_WIDTH, BLOCK_HEIGHT)) for i in range(NUM_BLOCKS)]
                score = 0

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= 5
    if keys[pygame.K_RIGHT]:
        paddle.x += 5

    # 패들 벽 충돌 처리
    if paddle.left < 0:
        paddle.left = 0
    elif paddle.right > SCREEN_WIDTH:
        paddle.right = SCREEN_WIDTH

    # 공 이동
    ball.x += ball_dx
    ball.y += ball_dy

    # 공 벽 충돌 처리
    if ball.left < 0 or ball.right > SCREEN_WIDTH:
        ball_dx *= -1
    if ball.top < 0:
        ball_dy *= -1

    # 공 패들 충돌 처리
    if ball.colliderect(paddle):
        ball_dy *= -1

    # 공 블록 충돌 처리
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_dy *= -1
            score += 10

    # 블록 그리기
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    # 패들 그리기
    pygame.draw.rect(screen, WHITE, paddle)

    # 공 그리기
    pygame.draw.circle(screen, WHITE, (ball.x + BALL_SIZE // 2, ball.y + BALL_SIZE // 2), BALL_SIZE // 2)

    # 점수 표시
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # 게임 오버 텍스트 표시
    if len(blocks) == 0:
        game_over_text = font.render("Game Over - Press SPACE to Restart", True, WHITE)
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, (SCREEN_HEIGHT - game_over_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(30)  # FPS를 30으로 수정
