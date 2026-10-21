/**
 * 역사 스토리 게임
 */
/**
 * 메인 화면 + 캐릭터 선택
 */
// A 버튼
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (page == 0) {
        character_screen()
    } else if (page == 1) {
        start_story()
    }
})
// 위쪽 버튼
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (page == 1) {
        selected += 0 - 1
        if (selected < 0) {
            selected = 3
        }
        character_screen()
    }
})
// 메인 화면
function main_screen () {
    page = 0
    bg = image.create(160, 120)
    bg.fill(8)
    bg.drawRect(5, 5, 150, 110, 5)
    bg.printCenter("HISTORY", 20, 5)
bg.printCenter("ADVENTURE", 38, 1)
// PLAY 버튼
    bg.fillRect(30, 62, 100, 28, 5)
    bg.drawRect(30, 62, 100, 28, 1)
    bg.printCenter("PLAY", 72, 14)
bg.printCenter("A: START", 102, 1)
scene.setBackgroundImage(bg)
}
// 아래쪽 버튼
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (page == 1) {
        selected += 1
        if (selected > 3) {
            selected = 0
        }
        character_screen()
    }
})
// 선택 완료 화면
function start_story () {
    page = 2
    bg3 = image.create(160, 120)
    bg3.fill(8)
    bg3.drawRect(5, 5, 150, 110, 5)
    bg3.printCenter("SELECTED", 25, 5)
bg3.printCenter(names[selected], 52, 1)
bg3.printCenter("STORY START!", 78, 5)
bg3.printCenter("B: BACK", 105, 1)
scene.setBackgroundImage(bg3)
}
// B 버튼
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (page == 1) {
        main_screen()
    } else if (page == 2) {
        character_screen()
    }
})
// 캐릭터 선택 화면
function character_screen () {
    let y: number;
page = 1
    bg2 = image.create(160, 120)
    bg2.fill(8)
    bg2.drawRect(5, 5, 150, 110, 5)
    bg2.printCenter("SELECT CHARACTER", 12, 5)
for (let i = 0; i <= 3; i++) {
        y = 26 + i * 19
        if (i == selected) {
            bg2.fillRect(18, y, 124, 18, 5)
            bg2.printCenter(names[i], y + 5, 14)
        } else {
            bg2.fillRect(18, y, 124, 18, 9)
            bg2.printCenter(names[i], y + 5, 1)
        }
    }
    bg2.printCenter("UP DOWN A:OK B:BACK", 107, 1)
scene.setBackgroundImage(bg2)
}
let bg2: Image = null
let bg3: Image = null
let bg: Image = null
let page = 0
let selected = 0
let names = [
"황옥",
"김상옥",
"안중근",
"윤봉길"
]
// 게임 시작
main_screen()
