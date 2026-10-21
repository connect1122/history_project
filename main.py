
# 역사 스토리 게임
# 메인 화면 + 캐릭터 선택

page = 0
selected = 0

names = [
    "황옥",
    "김상옥",
    "안중근",
    "윤봉길"
]


# 메인 화면
def main_screen():
    global page
    page = 0

    bg = image.create(160, 120)
    bg.fill(8)

    bg.draw_rect(5, 5, 150, 110, 5)

    bg.print_center("HISTORY", 20, 5)
    bg.print_center("ADVENTURE", 38, 1)

    # PLAY 버튼
    bg.fill_rect(30, 62, 100, 28, 5)
    bg.draw_rect(30, 62, 100, 28, 1)
    bg.print_center("PLAY", 72, 14)

    bg.print_center("A: START", 102, 1)

    scene.set_background_image(bg)


# 캐릭터 선택 화면
def character_screen():
    global page
    page = 1

    bg = image.create(160, 120)
    bg.fill(8)

    bg.draw_rect(5, 5, 150, 110, 5)
    bg.print_center("SELECT CHARACTER", 12, 5)

    for i in range(4):
        y = 26 + i * 19

        if i == selected:
            bg.fill_rect(18, y, 124, 18, 5)
            bg.print_center(names[i], y + 5, 14)
        else:
            bg.fill_rect(18, y, 124, 18, 9)
            bg.print_center(names[i], y + 5, 1)

    bg.print_center("UP DOWN A:OK B:BACK", 107, 1)

    scene.set_background_image(bg)


# 선택 완료 화면
def start_story():
    global page
    page = 2

    bg = image.create(160, 120)
    bg.fill(8)

    bg.draw_rect(5, 5, 150, 110, 5)

    bg.print_center("SELECTED", 25, 5)
    bg.print_center(names[selected], 52, 1)
    bg.print_center("STORY START!", 78, 5)
    bg.print_center("B: BACK", 105, 1)

    scene.set_background_image(bg)


# 위쪽 버튼
def on_up_pressed():
    global selected

    if page == 1:
        selected -= 1

        if selected < 0:
            selected = 3

        character_screen()

controller.up.on_event(
    ControllerButtonEvent.PRESSED,
    on_up_pressed
)


# 아래쪽 버튼
def on_down_pressed():
    global selected

    if page == 1:
        selected += 1

        if selected > 3:
            selected = 0

        character_screen()

controller.down.on_event(
    ControllerButtonEvent.PRESSED,
    on_down_pressed
)


# A 버튼
def on_a_pressed():
    if page == 0:
        character_screen()
    elif page == 1:
        start_story()

controller.A.on_event(
    ControllerButtonEvent.PRESSED,
    on_a_pressed
)


# B 버튼
def on_b_pressed():
    if page == 1:
        main_screen()
    elif page == 2:
        character_screen()

controller.B.on_event(
    ControllerButtonEvent.PRESSED,
    on_b_pressed
)


# 게임 시작
main_screen()
