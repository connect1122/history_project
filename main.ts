//  역사 스토리 게임
//  메인 화면 + 캐릭터 선택
let page = 0
let selected = 0
let names = ["황옥", "김상옥", "안중근", "윤봉길"]
//  메인 화면
function main_screen() {
    
    page = 0
    let bg = image.create(160, 120)
    bg.fill(8)
    bg.drawRect(5, 5, 150, 110, 5)
    bg.printCenter("EHFRU", 20, 5)
    bg.printCenter("ADVENTURE", 38, 1)
    //  PLAY 버튼
    bg.fillRect(30, 62, 100, 28, 5)
    bg.drawRect(30, 62, 100, 28, 1)
    bg.printCenter("PLAY", 72, 14)
    bg.printCenter("A: START", 102, 1)
    scene.setBackgroundImage(bg)
}

//  캐릭터 선택 화면
function character_screen() {
    let y: number;
    
    page = 1
    let bg = image.create(160, 120)
    bg.fill(8)
    bg.drawRect(5, 5, 150, 110, 5)
    bg.printCenter("SELECT CHARACTER", 12, 5)
    for (let i = 0; i < 4; i++) {
        y = 26 + i * 19
        if (i == selected) {
            bg.fillRect(18, y, 124, 18, 5)
            bg.printCenter(names[i], y + 5, 14)
        } else {
            bg.fillRect(18, y, 124, 18, 9)
            bg.printCenter(names[i], y + 5, 1)
        }
        
    }
    bg.printCenter("UP DOWN A:OK B:BACK", 107, 1)
    scene.setBackgroundImage(bg)
}

//  선택 완료 화면
function start_story() {
    
    page = 2
    let bg = image.create(160, 120)
    bg.fill(8)
    bg.drawRect(5, 5, 150, 110, 5)
    bg.printCenter("SELECTED", 25, 5)
    bg.printCenter(names[selected], 52, 1)
    bg.printCenter("STORY START!", 78, 5)
    bg.printCenter("B: BACK", 105, 1)
    scene.setBackgroundImage(bg)
}

//  위쪽 버튼
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (page == 1) {
        selected -= 1
        if (selected < 0) {
            selected = 3
        }
        
        character_screen()
    }
    
})
//  아래쪽 버튼
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (page == 1) {
        selected += 1
        if (selected > 3) {
            selected = 0
        }
        
        character_screen()
    }
    
})
//  A 버튼
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (page == 0) {
        character_screen()
    } else if (page == 1) {
        start_story()
    }
    
})
//  B 버튼
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    if (page == 1) {
        main_screen()
    } else if (page == 2) {
        character_screen()
    }
    
})
//  게임 시작
main_screen()
