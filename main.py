def other_character():
    global page, bg4
    page = 4
    bg4 = new_background()
    bg4.print_center(names[character], 31, 5)
    bg4.print_center("준비 중", 61, 1)
    bg4.print_center("B: 뒤로", 101, 1)
    scene.set_background_image(bg4)
def new_background():
    global bg
    bg = image.create(160, 120)
    bg.fill(8)
    bg.draw_rect(4, 4, 152, 112, 5)
    return bg
def title_screen():
    global page, bg2
    page = 0
    bg2 = new_background()
    bg2.print_center("독립운동", 20, 5)
    bg2.print_center("역사 게임", 38, 1)
    bg2.fill_rect(30, 64, 100, 28, 5)
    bg2.draw_rect(30, 64, 100, 28, 1)
    bg2.print_center("PLAY", 73, 1)
    bg2.print_center("A: 시작", 102, 1)
    scene.set_background_image(bg2)

def on_a_pressed():
    if page == 0:
        character_screen()
    elif page == 1:
        if character == 1:
            load_node(0)
        else:
            other_character()
    elif page == 2:
        result = option_targets[choice]
        if result >= 0:
            load_node(result)
        else:
            show_ending(result)
    elif page == 3:
        load_node(0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_up_pressed():
    global character, choice
    if page == 1:
        character = (character + 3) % 4
        character_screen()
    elif page == 2:
        choice = (choice + len(option_names) - 1) % len(option_names)
        draw_node()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_pressed():
    global character, choice
    if page == 1:
        character = (character + 1) % 4
        character_screen()
    elif page == 2:
        choice = (choice + 1) % len(option_names)
        draw_node()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_right_pressed():
    global secret_open
    if page == 2 and node == 2 and not (secret_open):
        secret_open = True
        option_names.append("D: 세계에 알리기")
        option_targets.append(-16)
        draw_node()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def draw_node():
    global bg5, stage_titles
    bg5 = new_background()
    stage_titles = ["1-1 혁신단",
        "1-2 상하이",
        "2-1 압록강",
        "2-2 종로경찰서",
        "3-1 삼판통",
        "3-2 남산 탈출",
        "4-1 효제동",
        "4-2 마지막 탄환"]
    bg5.print_center("김상옥", 6, 5)
    bg5.print_center(stage_titles[node], 19, 1)
    j = 0
    while j <= len(option_names) - 1:
        y2 = 34 + j * 18
        if j == choice:
            bg5.fill_rect(9, y2, 142, 17, 5)
            bg5.print_center(option_names[j], y2 + 4, 15)
        else:
            bg5.fill_rect(9, y2, 142, 17, 9)
            bg5.print_center(option_names[j], y2 + 4, 1)
        j += 1
    if node == 2 and not (secret_open):
        bg5.print_center("오른쪽: 비밀 선택?", 106, 5)
    elif node == 2 and secret_open:
        bg5.print_center("비밀 선택 해제", 106, 5)
    else:
        bg5.print_center("A: 결정 B: 설명", 107, 1)
    scene.set_background_image(bg5)

def on_b_pressed():
    if page == 1:
        title_screen()
    elif page == 2:
        game.show_long_text(scene_text, DialogLayout.FULL)
    elif page == 3 or page == 4:
        character_screen()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def load_node(new_node: number):
    global page, node, choice, secret_open, scene_text, option_names, option_targets
    page = 2
    node = new_node
    choice = 0
    secret_open = False
    if node == 0:
        # 1-1. 혁신단 조직과 일제의 추적
        scene_text = "1919~1920년 경성. 김상옥은 영덕철물점에서 독립운동에 참여한다. 혁신단을 조직한 뒤 일제 경찰의 추적이 거세졌다. 이제 어떤 길을 선택할까?"
        option_names = ["B: 공개 시위", "C: 경찰에 청원", "A: 비밀 조직"]
        option_targets = [-1, -2, 1]
    elif node == 1:
        # 1-2. 상하이에서 동지들과 협력
        scene_text = "상하이. 김상옥은 의열단과 연결되어 비밀 임무를 준비한다. 필요한 물자와 도움을 얻으려면 누구를 믿어야 할까?"
        option_names = ["B: 암시장 거래", "C: 배 단독 공격", "A: 동지들과 협력"]
        option_targets = [-3, -4, 2]
    elif node == 2:
        # 2-1. 압록강 도하와 숨겨진 선택지
        scene_text = "1922년 겨울. 압록강이 얼어붙었다. 김상옥은 국경 수비대의 눈을 피해 조선으로 돌아가야 한다. 어떤 경로를 선택할까? 어딘가에 숨겨진 선택지도 있다."
        option_names = ["B: 다리 검문소", "C: 밀수꾼 고용", "A: 밤에 건너기"]
        option_targets = [-5, -6, 3]
    elif node == 3:
        # 2-2. 종로경찰서 사건: 투탄 주체에 대한 역사적 이견 있음
        scene_text = "1923년 1월 12일, 종로경찰서에 폭탄이 터지고 주변 사람들이 다쳤다. 경성에는 삼엄한 경계가 펼쳐졌다. 폭탄을 던진 인물이 누구인지는 역사적으로 견해가 엇갈린다. 이 게임은 널리 알려진 서술을 바탕으로 한다."
        option_names = ["B: 정문으로 접근", "A: 서쪽 창문"]
        option_targets = [-7, 4]
    elif node == 4:
        # 3-1. 삼판통 은신처 포위: 열차 작전은 가상 분기
        scene_text = "1923년 1월 17일. 다무라 형사가 이끄는 일제 경찰이 삼판통 은신처를 포위했다. 탈출로가 좁혀지고 있다. 일부 선택지는 실제 역사와 다른 가상 이야기다."
        option_names = ["B: 열차 작전(가상)", "C: 뒷골목 탈출", "A: 지붕으로 탈출"]
        option_targets = [-15, -8, 5]
    elif node == 5:
        # 3-2. 남산 탈출과 안장사 승복, 효제동 은신
        scene_text = "김상옥은 눈 덮인 남산을 넘어 포위망을 벗어났다. 기록에 따르면 안장사에서 승복을 빌려 입고, 이혜수의 도움을 받아 효제동에 있는 이태성의 집으로 몸을 숨겼다."
        option_names = ["B: 남산에 남기", "C: 다리로 이동", "A: 승복으로 변장"]
        option_targets = [-9, -10, 6]
    elif node == 6:
        # 4-1. 효제동에서의 마지막 항전
        scene_text = "1923년 1월 22일. 경찰과 군인 약 1천 명이 효제동 은신처를 포위했다. 김상옥은 몇 시간 동안 홀로 맞서 싸웠다. 마지막 순간, 어떤 선택을 할까?"
        option_names = ["B: 마당으로 나가기", "C: 항복하기", "A: 지붕에서 항전"]
        option_targets = [-11, -12, 7]
    else:
        # 4-2. 마지막 탄환과 역사 엔딩
        scene_text = "마지막 탄환 하나가 남았다. 김상옥은 일제에 생포되지 않겠다고 결심한다. 역사 속 그의 최후는 모두가 살아남는 승리의 결말이 아니었다."
        option_names = ["B: 빈 총으로 돌진", "A: 마지막까지 항전"]
        option_targets = [-13, -14]
    draw_node()
    game.show_long_text(scene_text, DialogLayout.FULL)
def show_ending(result2: number):
    global page, label, bg6
    page = 3
    label = "가상 엔딩"
    if result2 == -1:
        title = "종로의 함정"
        details = "배드 엔딩 1. 낮에 무장 시위를 벌였지만 종로 네거리에서 경찰에 포위되었다. 실제 역사와 다른 가상 이야기다."
    elif result2 == -2:
        title = "거짓 약속"
        details = "배드 엔딩 2. 일제 경찰에게 청원서를 냈다가 오히려 붙잡혔다. 실제 역사와 다른 가상 이야기다."
    elif result2 == -3:
        title = "밀고자의 함정"
        details = "배드 엔딩 3. 암시장 상인이 비밀 모임을 밀고자에게 알렸다. 실제 역사와 다른 가상 이야기다."
    elif result2 == -4:
        title = "실패한 기습"
        details = "배드 엔딩 4. 상하이에서 홀로 배를 공격했으나 실패했다. 실제 역사와 다른 가상 이야기다."
    elif result2 == -5:
        title = "국경 검문"
        details = "배드 엔딩 5. 압록강 다리에서 국경 수비대가 짐을 수색해 정체를 알아냈다. 가상 이야기다."
    elif result2 == -6:
        title = "사라진 물자"
        details = "배드 엔딩 6. 고용한 밀수꾼이 물자를 가지고 달아났다. 실제 역사와 다른 가상 이야기다."
    elif result2 == -7:
        title = "정문의 실패"
        details = "배드 엔딩 7. 경찰서 정면으로 접근하다가 즉시 작전이 실패했다. 가상 이야기다."
    elif result2 == -8:
        title = "뒷골목 매복"
        details = "배드 엔딩 8. 뒷골목에도 경찰이 매복해 있어 탈출에 실패했다. 가상 이야기다."
    elif result2 == -9:
        title = "남산 포위"
        details = "배드 엔딩 9. 눈 덮인 남산의 은신처에 계속 머물다가 경찰에 포위되었다. 가상 이야기다."
    elif result2 == -10:
        title = "다리 검문"
        details = "배드 엔딩 10. 낮에 다리를 건너다 검문소에서 발각되었다. 실제 역사와 다른 가상 이야기다."
    elif result2 == -11:
        title = "마당의 항전"
        details = "배드 엔딩 11. 몸을 숨길 곳이 없는 마당에서 마지막 항전을 마쳤다. 가상 이야기다."
    elif result2 == -12:
        title = "체포"
        details = "배드 엔딩 12. 총을 내려놓은 김상옥이 일제 경찰에 체포되었다. 가상 이야기다."
    elif result2 == -13:
        title = "빈 탄창"
        details = "배드 엔딩 13. 탄환이 없는 총을 든 채 돌진했지만 뜻을 이루지 못했다. 가상 이야기다."
    elif result2 == -14:
        label = "역사 엔딩"
        title = "마지막 항전"
        details = "역사 엔딩. 1923년 1월 22일 효제동에서 김상옥은 오랜 항전 끝에 생포되지 않은 채 생을 마감했다. 그의 희생은 한국 독립운동의 역사에 남아 있다. 최후의 정확한 발언은 확인되지 않았다."
    elif result2 == -15:
        label = "대체 엔딩"
        title = "탈출 열차"
        details = "대체 역사 엔딩. 남대문역 근처에서 가상의 작전을 벌여 탈출에 성공했다. 실제 역사에는 없는 사건이다."
    else:
        label = "숨겨진 엔딩"
        title = "세계에 알리다"
        details = "비밀 엔딩. 일제 경찰의 고문을 고발하는 가상의 보고서가 국제연맹에 전달된다. 이 이야기에서 실제로 일어난 역사적 사건이 아니다."
    bg6 = new_background()
    bg6.print_center(label, 21, 5)
    bg6.print_center(title, 47, 1)
    bg6.print_center("A: 다시하기", 85, 5)
    bg6.print_center("B: 인물선택", 102, 1)
    scene.set_background_image(bg6)
    game.show_long_text(details, DialogLayout.FULL)
def character_screen():
    global page, bg3
    page = 1
    bg3 = new_background()
    bg3.print_center("인물 선택", 10, 5)
    for i in range(4):
        y = 27 + i * 19
        if i == character:
            bg3.fill_rect(16, y, 128, 18, 5)
            bg3.print_center(names[i], y + 4, 15)
        else:
            bg3.fill_rect(16, y, 128, 18, 9)
            bg3.print_center(names[i], y + 4, 1)
    bg3.print_center("A: 선택 B: 뒤로", 107, 1)
    scene.set_background_image(bg3)
"""

MakeCode Arcade Python - 독립운동 역사게임

"""
"""

김상옥: 8개 장면, 선택지, 역사 엔딩과 가상 엔딩

"""
"""

별도 확장 기능 없이 image.print_center / game.show_long_text 사용

"""
"""

참고: 기기나 버전에 따라 한글 글꼴 표시가 제한될 수 있음

"""
"""

화면: 0 메인, 1 인물 선택, 2 김상옥 이야기, 3 엔딩, 4 준비 중

"""
bg3: Image = None
bg6: Image = None
label = ""
scene_text = ""
stage_titles: List[str] = []
bg5: Image = None
secret_open = False
choice = 0
bg2: Image = None
bg: Image = None
bg4: Image = None
page = 0
option_targets: List[number] = []
option_names: List[str] = []
node = 0
character = 0
# 비어 있는 리스트 대신 자료형이 분명한 값으로 초기화
names = ["황옥", "김상옥", "안중근", "윤봉길"]
option_names = ["계속", "뒤로"]
option_targets = [1, 0]
title_screen()