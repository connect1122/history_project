# 독립의 길: 황옥 - MakeCode Arcade Python 완성본
# 기존 Python 코드를 모두 지우고 이 파일 전체를 붙여넣으세요.
# A: 다음/확정, B: 이전 본문/로비, 방향키: 선택지 전환
# 인물 선택 화면 없음. 신뢰 회복 60% -> 1-A. 공격 성공 각각 70%.
# 밀정 이력: 1-B-A에 도달하면 기록. 새 게임에서만 초기화.
# 원문 기반 역사 선택 게임이며, 분기와 확률은 게임용 창작입니다.
# 모든 한글은 내장 Galmuri9 픽셀 데이터로 표시됩니다.
# 글꼴 데이터와 라이선스는 파일 하단에 포함합니다.
title_image = img("""
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc
    cfccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfc
    cfc5555cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc5555cfc
    cfcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc666cccccccccccccccccccccccccccfc
    cfcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc666ccccccccc777cccccccccccccccfc
    cfcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc777cccccccccccccccfc
    cfccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfc
    cfccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfc
    cfcccccccccccccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcccccccccccccfc
    cfcccccccccccccdccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdcccccbbbcccccfb
    cfcccccccccccccdccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdcccccbbbcccccfb
    6f6ccccccccccccdcc5cccccccccccccccccccccccccccccccccccccccccccccccccccccccdddcccccccccccccdddccccccccccccccccccdddccccccccccccccccccccccccccccccdcccccccccccccfc
    6f6777cccccccccdccccccccccccccccccccccccccccccccdddddddddddcccccdddddddcccdddfccccccccccccdddfcccccccddddddddccdddfcccccccccccccccccccccccccccccdcccccccccccccfc
    cfc777cccccccccdccccccccccccccccccccccccccccccccdddddddddddfccccdddddddfccdddfccccddddccccdddfcccccccdddddddffcdddfcccccccccccccccccccccccccccccdcccccccccccccfc
    cfcccccccccccccdccccccccccccccccccccccccccccccccddffffffffffcccccffffddfccdddfccddddddddccdddfccccccccffffddfccdddfcccccccccccccccccccccccccccccdcc66cccccccccfc
    cfcccccccccccccdccccccccccccccccccccccccccccccccddfcccccccccccccdddddddfccdddfccddffffddfcdddfcccccccccccdddfccdddfcccccccccccccccccccccccccccccdcc666ccccccccfc
    cfc666cccccccccdccccccccccccccccccccccccccccccccdddddddddddcccccdddddddfccdddfccddfcccdddcdddfcccccccccccdddfccdddfcccccccccccccccccccccccccccccdcc666ccccccccfc
    bfb666cccccccccdccccccccccccccccccccccccccccccccdddddddddddfccccddffffffccdddfccddfcccdddfdddfcccccccccddddffccdddfcccccccccccccccccccccccccccccdccccccccccbbbfc
    bfbccccccccc7ccdcccccccccccccccccccccccccccccccccfffddffffffccccddfcccccdcdddfccdddcccddffdddfccccccddddddffcccdddfcccccccccccccccccccccccccccccdccccccccccbbbfc
    cfcccccccccc7ccdccccccccccccccccccccccccccccccccccccddfcccccccccdddddddddfdddfccddddddddfcdddfccccccddddfffccccdddfcccccccccccccccccccccccccccccdcccccccccccccfb
    cfcccccccccccccdccccccccccccccccccccccccccccccdddddddddddddddcccdddddddddfdddfcccfddddfffcdddfcccccccffffcccccccfffcccccccccccccccccccccccccccccdcccccccccccc7fb
    cfcccccccccc7ccdccccccccccccccccccccccccccccccdddddddddddddddfcccfffffffffcfffcccccffffcccdddfccccccccddddddddddddccccccccccccccccccccccccccccccdccbbcccccccc7fc
    cfcccccccccc7ccdcccccccccccccccccccccccccccccccfffffffffffffffcccdddccccccdddcccccccccccccdddfccccccccddddddddddddfcccccccccccccccccccccccccccccdccbbccccbbbccfc
    cfbbcccccccccccdcccccccccccccccccccccccccccccccddddddddddddccccccddddddddddddfcddddddddddcdddfcccccccccffffffffdddfcccccccccccccccccccccccccccccdcccccccccbbccfc
    7fbbbccccccccccdcccccccccccccccccccccccccccccccddddddddddddfcccccddddddddddddfcdddddddddffdddfccccccccddddddddddddfcccccccccccccccccccccccccccccdcccccccccccccfc
    7fbbb666cccccccdccccccccccccccccccccccccccccccccfffffffffddfcccccdddffffffdddfccfffffffffcdddfccccccccddddddddddddfcccccccccccccccccccccccccccccdcccccccccccccfc
    cfccc666cccccccdcccccccccccccccccccccccccccccccccccccccccddfcccccdddfcccccdddfccccccccccccdddfccccccccdddffffffffffcccccccccccccccccccccccccccccdcc777ccccccccfc
    cf66cccccccccccdcccccccccccccccccccccccccccccccccccccccccddfcccccddddddddddddfccccccccccccdddfccccccccddddddddddddccccccccccccccccccccccccccc5ccdcc777ccccccccfc
    ff66fccccccccccdcccccccccccccccccccccccccccccccccccccccccddfcccccddddddddddddfccccccccccccdddfccccccccddddddddddddfcccccccccccccccccccccccccccccdcccccc777ccccfc
    6f6cc777fffffccdccccccccccccccccccccccccccccccccccccccccccffccccccffffffffffffcccccccccccccfffcccccccccffffffffffffcccccccccccccccccccccccccccccdcccccc777ccccfc
    6f6bb777bbbbbccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccbbbbbbbbbbbfb
    bf776bbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbfb
    bf776bb666bbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc7bbbbbbbbbbfb
    bfcccbb666bbbbbbbbbb666bb7666bbbbbbbcccfffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb5555555dddddddddd5555555777fbbbbbbbbbfb
    ffcccb6777bbbbbbbbbbbbbb7ccc6bbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc5dddddddddddd777555bbbfbb777bbbbfb
    bfbbbf666ffffffbbbbbbbbbbcccbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccddddddddddddd77755666bfbb777bbbbfb
    bfbbbbbbbcccbbbffffffffffbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccddddddddddcccdd5556666fbbbbbbbbbfb
    bfbbbbbbbcccbbbbbbbbbbbbbffbbbffffccdccdcdcdddddddddcddcccdddddcddcccccdccccddcddcddcccdccdcdddcccccdddcdccdccddcccdccdddcdddcddddddddddcccddd555666fbbbbbbbbbfb
    bfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccdccdcdcdcccccdccdccdccdcdcdcdccccccdcccccdcdcdccdccdccdcdcdccccdccccdccdcdccdccdcdccccdcccdddddddddddddddd555ffffbbbbbbbbbfb
    bfbbbbcccbbbb666bbbbbbbbbbbbbbbbbbccddddcdccdddccdccdccdccddcccdcccccccdccccccdccdccdccdccdcddcccccdccccddddcdccdccdcdccccdddcddddddddddddddddd55ffffbbbbbbbbbfb
    bfbbbbcccbbbb666666bbbbbbbbbbbbbbbccdccdcdccccdccdccdccdccdcdccdccccccdcccccccdccdccdccdccdcdcdccccdccccdccdcdccdccdcdccccdcccddddddddddddddddd55ffffbbbbbbbbbfb
    bfbbbbbbbbbbbbbb666bbbbbbbbbbbbbbbccdccdcdcddddccdcccddcccdcddcdccccccdcccccccdcccddccccddccdcddccccdddcdccdccddcccdccdddcdddcddddddddddddddddd55ffffbbbbbbbbbfb
    bfbbbbbbbbbbbbbbbbbbbbbbbbbbffffffccccccccccccccccccccccccccccccccccccdcccccccccccccccccccccccccccccccccccccccccccccccccccccccddddddddddddddddd55fffdddbbbdddbfb
    bfbbbbbbbbbbbbbbbbbbbbbbbbbbffffffccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfdddddddddddddddd55fffdddbbbdddbfb
    efeeeeeeeeeeeeeeeeeeeeeeeeeeffffffccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdfffffffffdddfffffffffdddfffdddffe
    efeeeeeeeeeeeeeeeeeeeeeeeeeeffffffccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccddddffffffdddfffffffffdddfffdddffe
    efeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeee555eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffdddddffffffdddfffffffffdddfffdddffe
    efeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeee555eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee555555ffffffdddddddddd5555fffdddeeedddefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffdddddddddddddddddddddddddddddddd555ddddddddddddddddddddddddddddddddefffffffffffdddddddddddddd55555fffdddeeedddefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeee555eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffff5dddddddddddd555555ffffeeeeeeeeefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeee555eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffdddddddd5555555ffffeeeeeeeeefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffdddddd55555555effffeeeeeeeeefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffff5555555555555eeffffeeeeeeeeefe
    4f444444444444e444444444444efffffffffffffffffffff444444444e4444444e444444444444444444444e4e444444444e444444444444fffffffffffffffff555555555555e44ffff444444e44f4
    4f4444444444444b444444444444fffdddddddddddddddfebb4444444444444444444444444444444444444444444e44444444444444444e4fffffffffffffffff555555555554444ffff444444444f4
    4f444444444444bbb44444444444fffdddddddddddddddffbbb444444444444444444e444444444444444444444444444444d4e44444e4444fffffffffffffffff555555555444444ffff444444444fb
    4f4444444444bbbbbbee4444444efffdddddddddddddddffbbbbb444444444444444444444444444b4444444e4444e444e444444444444444fffffffffffffffff55555554e44e444ffff4444444d4fb
    4f444444444bbbbbbbb444444444fffdddfdddddddfdddffbbbbbbb44444444444444444444444bbbb4444444444444444444444444444444fffffffffffffffff444444444444444ffff4444444bbfb
    4f4444444ebbbbbbbbbbb4444444fffdddeeeeeeeeddddffbbbbbbbb4444444444e444444444bbbbbbbb44444444444444444444444444444ddddddddddddddddd444444444444444ffff444444bbbfb
    4f444d44bbbbbbbbbbbbbb444444fffdddeeeeeeeedddddbbbbbbbbbbb4444444444444444bbbbbbbbbbb444444444444444444444444444bddddddddddddddddd444444444444444ffff4444bbbbbfc
    4f44444bbbbbbbbbbbbbbbb4444444dddddddddddddddddbbbbbbbbbbbb4c444444444444bbbbbbbbbbbbb444444444444444444444444bbbddddddddddddddddde44444444444444ffff444bbbcccfc
    4f444bbbbbbbbbbbbbbbbbcb444444dddddddddddddddddbbbbbbbbbbbccccc44444444bbbbbbbbbbbbbbbbb44444444444444444444bbbbbddddddddddddddddd444444444444444ffff4ccccccccfc
    efeebbbbbbbbbbbbbbbcccccbefeeedddddddeeeeddddddbbbbbbbbbcccccccceeeeebbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeceeeebbbbbbdddddddddddddddddbeeeeeeeeeeeeeeffffcccccccccfc
    efebbbbbbbbbbbbbbcccccccccffffdddddddddddddddddfffffbbccccccccccccebbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeccccccbbbbbbbddddfdddddddfddddbbbeeeeeeeeecccffffcccccccccfc
    efbbbbbbbbbbbbccccccccccccffffdddddddddddddddddfffffccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbeeeeeecccccccccccbbbbdddddddddddddddddbbbbbeeccccccccffffcccccccccfc
    bfbbbbbbbbbcccccccccccccccfffedddddddddddddddddeefffcccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbeeeecccccccccccccccbdddddddddddddddddbbbccccccccccccffffcccccccccfc
    bfbbbbbbcccccccccccccccccffffedddddddddddddddddeefffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddcccccccccccccccffffcccccccccfc
    bfbbbbcccccccccccccccccccffffedddddddeeeeeeeeeeeeffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddcccccccccccccccffffcccccccccfc
    bfbccccccccccccccccccccccffffedddddddddeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddeeeeddddddcccccccccccccccffffcccccccccfc
    cfcccccccccccccccccccccccffffdddddddddddeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddddddddddddfffccccccccccccffffcccccccccfc
    cfcccccccccccccccccccccccffffeddddddddddddeeeeeeefffffbffffffffbffffffffbffffffffbffffffffbffffffffbffffffffbffffdddddddddddddddddfffccccccccccccffffcccccccccfc
    cfcccccccccccccccccccccccffffeddddddddddddeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddddddddddddfffccccccccccccffffcccccccccfc
    cfcccccccccccccccccccccccfffeeeddddddddddeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbb11111111bbbbfffbbbbbbbbbbbbffffbbbbbbbbbfb
    cfccccccccccccccccccccccffffeeeddddddddddeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbb1111111bbbbbffffbbbbbbbbbbbffffbbbbbbbbbfb
    cfccccccccccccccccccccccffffeeeedddddddddeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbb111111bbbbbffffffffffffffffffffffffffffff
    bfbbbbbbbbbbbbbbbbbbbbbbffffeeeeddddddddeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbb111111bbbbbffffffffffffffffffffffffffffff
    bfbbbbbbbbbbbbbbbbbbbbbbffffeeeeedddddddeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbb11111bbbbbbffffffffffbffffffffbffffffffff
    ffffffffffffffffffffffffffffeeeeeeddddddeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbb11211bbbbbbffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffbffffffffbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffeffeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeefffffeeeeeeeeeeffffeeeeeeeeefe
    fffffffffffffffffffffffffffeffeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeefffffeeeeeeeeeeffffeeeeeeeeefe
    fffffffffffffffffffffffffffeffeeddddddddddddddddddddddddddddddfdffddddddddddffddddddddddddddddddddddddffddddddddddddddddddddddddeeffffffffffffffffffffffffffffff
    efeeeeeeeeeeeeeeeeeeeefffffeffeedddddddfddddddddddddddddddddddfdffdddffffdddffdddddddddddddffddffffffdffddddddddddddddddddddddddeeffffffdddddddddffffdddddddddfd
    efeeeeeeeeeeeeeeeeeeeefffffeffeedddddddfffddddddddddddddfffffdfdffddffddffddffdddddddffddddffddddffdddffddddddddddddddddddddddddeeffffffdddddddddffffdddddddddfd
    fffffffffffffffffffffffffffeffeedddddddffffddddddddddddddddffdfdffddfddddfddffdddddddffddddffddddffdddffffddddddddddddddddddddddeeffffffdddddddddffffdddddddddfd
    dfddddddddddddddddddddfffffeffeedddddddffffffddddddddddddddfddfdffddfdddffddffdddddddffddddffdddffffddffddddddddddddddddddddddddeeffffffdddddddddffffdddddddddfd
    dfddddddddddddddddddddddddddffeedddddddffffffffdddddddddddfffffdffddffffffddffdddddddffddddffddfffdffdffddddddddddddddddddddddddeeffffffdddddddddffffdddddddddfd
    dfdddfeffdddddddddddddddddddffeedddddddffffffdddddddddddddffddfdffdddffffdddffdddddddfffdddffddffddffdffddddddddddddddddddddddddeeffffffdddddddddffffddfeffdddfd
    dfdddfeffdddddddddddddddddddffeedddddddffffddddddddddddddffdddfdffddddddddddddddddddffdfdddffddfddddddffddddddddddddddddddddddddeefffffffddddddddffffddfeffdddfd
    dfdddfeffdddddddddddddddddddffeedddddddfffddddddddddddddffddddfdffddddffffffffdddddfffdffddffdddddddddddddddddddddddddddddddddddeefffffffddddddddffffddfeffdddfd
    dfdddfeffdddddddddddddddddddffeedddddddfddddddddddddddddfdddddfdffddddfdddddffdddddffdddffdffdddffffffffddddddddddddddddddddddddeefffffffddddddddffffddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeddddddddddddddddddddddddddddddfdffddddfdddddffdddddfdddddddffdddddddddffddddddddddddddddddddddddeefffffffddddddddffffddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeddddddddddddddddddddddddddddddfdffddddfdddddffdddddddddddddffdddddddddffddddddddddddddddddddddddeefffddddddddddddffffddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeddddddddddddddddddddddddddddddddffddddffffffffdddddddddddddffdddddddddffddddddddddddddddddddddddeefffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeefffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeefffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeefffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddfeffdddfd
    dfdddfeffdddddddddddddddddddffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddddddddddddfeffdddfd
    dfdddfeffddddddddddddddddddddddfeffffddddddddbbbbbbbbbbbbbbbddbdddddbbbdddddbbdbdbbbbbbbbbbddbbbbbbbbbbddddddbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe
    dfdddfeffddddddddddddddddddddddfeffdddddddbbbbbbbbdbbbbbdbdbddbdbbbbbbbdbbbdbbdbdddddbbdddbddbbbbdbbdbbbbdbbdbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeededeeeededbddbdddddbbbbddddbdbbbbbbbbbbbdbddbbbbdbbdbbbbdbbddbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeededeeeeddddddbdddddbbdddddddbbdddddddbddddddbbbbdbbdbbbdbdbdbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefe
    efeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddeeeededbddbbbbbbbbbbbbbdbbbbbbdbbbbdbbbddbbbbddbdbbbbbbbdbbbbbbbbbbbbbbbbfeffbbbbbbbbbddddffffdddddfeffdddfd
    dfdddfeffddddddddddddddfffdddddfeffbbbbbbbbbbbbbdbbbdbbbdddbdddddddddbbbddddbbbbbdbddbbdddbddbbbdbdddbbbdddddbbbbbbbbbbbbbbbbfeffbbbbbbbbbbbbddddfffdddfeffdddfd
    dfd5555ffddddddddddddfffddddbbbfeffbbbbbbbbbbbbbdbbbdbbbbbbbddbdbbbbbbbdddddbbbbdddddbbbbbbddbbbbbbbdbbbbbbbdbbbbbbbbbbbbbbbbfeffbbbbbbbbbbbbbbddddfffffe5555dfd
    dfdddfeffddddddddddfffdddbbbbbbfeffbbbbbbbbbbbbbbbbbbbbbbbbbddbdddddbbbdddddbbbbdddddbbbbbbddbbbbbbbdbbbbbbbdbbbbbbbbbbbbbbbbfeffbbbbbbbbbbbbbbbbbddddffeffdddfd
    dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd
    dddddfeffddddddfffddbbbbbbbbbbbfeffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfeffbbbbbbbbbbbbbbbbbbbbbbfefffffdd
""")

font_width: List[number] = [4,4,4,8,4,5,4,4,6,4,6,7,6,6,4,5,6,6,6,6,6,6,5,6,2,3,6,6,6,5,5,5,6,6,6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
font_bits: List[number] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,2,2,0,0,0,5,5,0,0,0,0,0,0,0,0,0,0,34,37,21,18,8,36,84,82,34,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,4,4,4,2,2,2,1,1,1,0,0,0,14,17,17,17,17,17,17,17,14,0,0,0,3,2,2,2,2,2,2,2,2,0,0,0,15,16,16,16,14,16,16,16,15,0,0,0,17,17,17,17,17,62,16,16,16,0,0,0,14,1,1,1,15,17,17,17,14,0,0,0,31,16,16,8,4,4,4,4,4,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,7,8,8,4,2,2,0,2,2,0,0,0,4,4,10,10,10,31,17,17,17,0,0,0,15,17,17,17,15,17,17,17,15,0,0,0,0,0,0,15,16,30,17,17,30,0,0,0,0,0,0,30,1,1,1,1,30,0,0,0,16,16,16,30,17,17,17,17,30,0,0,0,0,0,0,14,17,31,1,1,30,0,0,0,12,2,2,15,2,2,2,2,2,0,0,0,0,0,0,30,17,17,17,30,16,15,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,15,17,17,17,17,17,0,0,0,0,0,0,14,17,17,17,17,14,0,0,0,0,0,0,15,17,17,17,15,1,1,0,0,0,0,0,13,3,1,1,1,1,0,0,0,0,0,0,14,1,6,8,8,7,0,0,0,0,2,2,15,2,2,2,2,12,0,0,0,0,0,0,17,17,17,17,17,30,0,0,0,0,0,0,17,17,10,10,4,4,0,0,0,0,0,0,17,17,10,10,4,4,3,0,0,159,144,144,144,392,136,132,131,128,0,0,0,159,144,400,136,135,0,254,128,128,0,0,0,159,144,400,136,135,128,2,2,254,0,0,0,159,144,400,136,135,0,254,2,254,0,0,0,159,400,136,135,0,254,248,6,254,0,0,0,159,144,400,136,135,0,254,130,254,0,0,0,159,144,400,136,135,0,124,130,124,0,0,0,159,400,136,135,0,254,126,2,254,0,0,0,159,144,144,240,136,136,132,131,128,0,0,0,159,144,240,136,135,128,2,2,254,0,0,0,159,240,136,135,0,254,248,6,254,0,0,0,159,144,240,136,135,0,254,130,254,0,0,0,159,144,240,136,135,128,16,40,198,0,0,0,335,328,328,376,328,324,324,323,320,0,0,0,335,328,376,324,323,0,68,170,273,0,0,0,159,144,240,144,136,232,132,131,128,0,0,0,159,240,144,232,135,0,254,128,128,0,0,0,159,240,144,232,135,128,2,2,254,0,0,0,159,240,136,231,128,254,248,6,254,0,0,0,159,240,144,232,135,0,124,130,124,0,0,0,335,328,376,328,328,372,324,323,320,0,0,0,254,128,128,128,144,144,16,511,0,0,0,0,254,128,144,16,511,0,124,130,124,0,0,0,159,144,144,144,404,132,132,191,128,0,0,0,159,144,404,132,191,128,2,2,254,0,0,0,159,144,148,132,191,0,124,130,124,0,0,0,254,128,128,128,511,16,16,16,16,0,0,0,254,128,128,128,511,16,254,128,128,0,0,0,254,128,128,511,16,130,254,130,254,0,0,0,254,128,128,128,128,128,0,511,0,0,0,0,254,128,128,128,511,0,2,2,254,0,0,0,254,128,128,511,0,130,254,130,254,0,0,0,159,144,144,144,136,136,132,131,128,0,0,0,159,144,144,136,135,128,2,2,254,0,0,0,159,144,144,136,135,0,254,130,254,0,0,0,159,146,146,146,402,146,146,137,128,0,0,0,351,338,338,370,338,338,338,329,320,0,0,0,238,136,136,0,511,16,18,2,254,0,0,0,238,136,136,511,0,254,248,6,254,0,0,0,238,136,136,511,0,254,126,2,254,0,0,0,129,129,129,129,385,129,129,191,128,0,0,0,129,129,385,129,191,128,2,2,254,0,0,0,129,385,129,191,0,254,248,6,254,0,0,0,129,129,385,129,191,0,254,130,254,0,0,0,321,321,321,321,449,321,321,351,320,0,0,0,321,321,449,321,351,320,2,2,510,0,0,0,129,129,385,129,129,385,129,191,128,0,0,0,129,129,129,241,129,129,129,159,128,0,0,0,129,129,225,129,159,0,254,130,254,0,0,0,321,321,321,369,321,321,321,351,320,0,0,0,2,2,2,2,254,16,16,511,0,0,0,0,2,2,254,16,511,0,254,68,254,0,0,0,2,2,2,254,0,511,16,16,16,0,0,0,2,2,2,2,254,0,0,511,0,0,0,0,2,2,254,0,511,0,2,2,254,0,0,0,2,2,254,0,511,0,124,130,124,0,0,0,2,2,254,0,511,0,254,40,198,0,0,0,129,129,129,129,129,129,129,159,128,0,0,0,159,129,129,129,385,129,129,159,128,0,0,0,159,129,385,129,159,128,2,2,254,0,0,0,159,385,129,159,0,254,248,6,254,0,0,0,159,129,385,129,159,0,124,130,124,0,0,0,351,321,321,321,449,321,321,351,320,0,0,0,159,129,129,241,129,129,129,159,128,0,0,0,159,129,225,129,159,128,2,2,254,0,0,0,351,321,321,369,321,321,321,351,320,0,0,0,254,2,2,2,254,16,16,511,0,0,0,0,254,2,254,16,511,0,254,128,128,0,0,0,254,2,254,16,511,130,254,130,254,0,0,0,254,2,254,16,511,0,124,130,124,0,0,0,159,129,129,129,159,132,132,191,128,0,0,0,159,129,129,159,132,191,0,2,254,0,0,0,159,129,159,132,191,254,248,6,254,0,0,0,254,2,2,254,0,511,16,16,16,0,0,0,159,129,129,159,128,191,132,132,132,0,0,0,159,129,159,128,191,132,16,40,198,0,0,0,254,2,254,511,0,254,248,6,254,0,0,0,254,2,254,0,511,0,124,130,124,0,0,0,159,129,129,129,159,0,124,130,124,0,0,0,191,137,137,137,393,137,137,191,128,0,0,0,191,137,233,137,191,128,2,2,254,0,0,0,254,18,254,0,511,0,16,40,198,0,0,0,159,144,144,159,385,129,129,159,128,0,0,0,159,144,415,129,159,0,254,128,128,0,0,0,159,144,415,129,159,128,2,2,254,0,0,0,159,144,415,129,159,0,254,130,254,0,0,0,351,336,336,351,449,321,321,351,320,0,0,0,159,144,144,159,225,129,129,159,128,0,0,0,159,144,223,129,159,128,2,2,254,0,0,0,159,144,240,159,129,225,129,159,128,0,0,0,159,240,159,225,159,0,254,128,128,0,0,0,159,240,159,225,159,128,2,2,254,0,0,0,254,128,254,2,254,16,16,511,0,0,0,0,254,248,6,254,16,511,0,254,128,0,0,0,159,144,159,129,159,132,132,191,128,0,0,0,254,128,254,2,254,68,68,511,0,0,0,0,254,128,254,2,254,0,511,68,68,0,0,0,254,128,254,2,254,0,0,511,0,0,0,0,254,248,6,254,0,511,0,2,254,0,0,0,254,248,6,511,0,254,248,6,254,0,0,0,254,248,6,254,511,0,254,130,254,0,0,0,159,144,144,159,129,129,129,159,128,0,0,0,159,144,159,129,159,128,2,2,254,0,0,0,159,144,159,129,159,130,254,130,254,0,0,0,159,145,145,145,401,145,145,159,128,0,0,0,159,145,401,145,159,0,254,128,128,0,0,0,159,145,401,145,159,128,2,2,254,0,0,0,159,145,401,145,159,64,498,162,78,0,0,0,159,401,145,159,0,254,248,6,254,0,0,0,159,145,401,145,159,0,124,130,124,0,0,0,159,401,145,159,0,254,126,2,254,0,0,0,159,145,241,145,145,241,145,159,128,0,0,0,159,241,145,241,159,128,2,2,254,0,0,0,159,241,145,241,159,0,124,130,124,0,0,0,254,130,130,130,254,16,16,511,0,0,0,0,254,130,254,16,511,0,254,128,128,0,0,0,254,130,254,16,511,254,248,6,254,0,0,0,254,130,254,16,511,0,254,130,254,0,0,0,254,130,254,16,511,0,16,40,198,0,0,0,254,130,130,254,0,511,16,16,16,0,0,0,254,130,254,0,511,16,18,2,254,0,0,0,254,130,254,0,511,16,254,2,254,0,0,0,159,145,145,145,145,145,145,159,128,0,0,0,159,145,145,145,159,128,2,2,254,0,0,0,159,145,145,145,159,0,254,2,254,0,0,0,159,145,145,159,0,254,248,6,254,0,0,0,145,145,145,159,401,145,145,159,128,0,0,0,145,159,401,145,159,128,2,2,254,0,0,0,145,159,401,145,159,0,254,2,254,0,0,0,145,415,145,159,0,254,248,6,254,0,0,0,145,415,145,159,0,238,140,130,142,0,0,0,145,159,401,145,159,0,124,130,124,0,0,0,337,337,337,351,465,337,337,351,320,0,0,0,145,145,145,255,145,145,145,159,128,0,0,0,145,255,145,159,0,130,254,130,254,0,0,0,145,255,145,241,159,128,2,2,254,0,0,0,130,254,130,130,254,16,16,511,0,0,0,0,130,254,130,254,16,511,0,254,128,0,0,0,130,254,130,254,16,511,0,2,254,0,0,0,130,254,130,254,0,511,16,16,16,0,0,0,130,254,130,254,0,511,16,2,254,0,0,0,130,254,130,511,16,254,248,6,254,0,0,0,130,254,130,511,16,254,126,2,254,0,0,0,145,145,145,159,145,145,145,159,128,0,0,0,149,149,149,159,405,149,149,159,128,0,0,0,149,415,149,159,0,254,248,6,254,0,0,0,132,132,132,132,394,138,145,145,128,0,0,0,132,388,138,145,0,254,248,6,254,0,0,0,132,132,388,138,145,0,124,130,124,0,0,0,324,324,324,324,458,330,337,337,320,0,0,0,324,324,452,330,337,0,510,256,256,0,0,0,324,324,452,330,337,0,252,258,252,0,0,0,132,132,132,228,138,138,145,145,128,0,0,0,132,132,228,138,145,0,254,128,128,0,0,0,132,132,228,138,145,128,2,2,254,0,0,0,132,228,138,145,0,254,248,6,254,0,0,0,132,132,228,138,145,0,124,130,124,0,0,0,16,16,40,68,130,16,16,511,0,0,0,0,16,40,198,16,511,0,254,128,128,0,0,0,16,40,68,130,0,511,16,16,16,0,0,0,16,40,198,0,511,16,18,2,254,0,0,0,16,40,198,0,511,16,254,130,254,0,0,0,132,138,145,191,4,130,254,130,254,0,0,0,16,40,198,0,511,130,254,130,254,0,0,0,132,132,132,132,138,138,145,145,128,0,0,0,132,132,132,138,145,0,254,128,128,0,0,0,132,132,132,138,145,128,2,2,254,0,0,0,132,132,138,145,0,254,248,6,254,0,0,0,132,132,132,138,145,0,254,130,254,0,0,0,138,138,138,138,405,149,149,149,128,0,0,0,142,145,145,145,401,145,145,142,128,0,0,0,142,145,401,145,142,0,254,128,128,0,0,0,142,145,401,145,142,128,2,2,254,0,0,0,142,145,401,145,142,64,498,162,78,0,0,0,142,401,145,142,0,254,248,6,254,0,0,0,142,145,401,145,142,0,68,170,273,0,0,0,142,145,401,145,142,0,254,68,254,0,0,0,142,145,401,145,145,401,145,142,128,0,0,0,142,401,145,401,142,0,254,128,128,0,0,0,142,401,145,401,142,0,124,130,124,0,0,0,142,145,145,241,145,145,145,142,128,0,0,0,142,145,241,145,142,0,254,2,254,0,0,0,142,241,145,142,0,74,78,170,286,0,0,0,142,145,241,145,142,0,68,170,273,0,0,0,334,337,337,369,337,337,337,334,320,0,0,0,334,337,369,337,334,320,2,2,510,0,0,0,142,145,241,145,145,241,145,142,128,0,0,0,142,241,145,241,142,0,254,128,128,0,0,0,142,241,145,241,142,128,2,2,254,0,0,0,142,241,145,238,128,254,248,6,254,0,0,0,142,241,145,241,142,0,68,170,273,0,0,0,142,241,145,241,142,0,124,130,124,0,0,0,334,337,369,337,337,369,337,334,320,0,0,0,124,130,130,130,124,16,16,511,0,0,0,0,124,130,124,16,511,0,254,128,128,0,0,0,124,130,124,16,511,0,2,2,254,0,0,0,124,130,124,16,511,238,172,162,238,0,0,0,142,145,145,145,398,132,132,191,128,0,0,0,142,145,398,132,191,128,2,2,254,0,0,0,142,145,398,132,191,0,68,170,273,0,0,0,124,130,130,130,124,68,68,511,0,0,0,0,124,130,124,68,511,0,124,130,124,0,0,0,124,130,130,124,0,511,16,16,16,0,0,0,124,130,124,0,511,16,254,128,128,0,0,0,124,130,124,0,511,16,18,2,254,0,0,0,124,130,124,511,16,254,248,6,254,0,0,0,124,130,124,0,511,16,254,130,254,0,0,0,142,145,145,142,128,191,132,228,132,0,0,0,142,145,142,191,228,132,2,2,254,0,0,0,142,145,142,191,228,132,68,170,273,0,0,0,142,145,145,142,128,191,132,132,132,0,0,0,124,130,130,124,0,511,68,68,68,0,0,0,124,130,130,130,124,0,0,511,0,0,0,0,124,130,124,0,511,0,2,2,254,0,0,0,124,130,124,511,0,254,248,6,254,0,0,0,124,130,124,0,511,0,254,130,254,0,0,0,142,145,145,145,142,128,128,191,128,0,0,0,142,145,145,145,145,145,145,142,128,0,0,0,142,145,145,145,142,128,2,2,254,0,0,0,142,145,145,142,0,254,248,6,254,0,0,0,142,145,145,142,0,78,508,162,78,0,0,0,142,145,145,145,142,0,254,130,254,0,0,0,142,145,145,142,0,130,254,130,254,0,0,0,142,145,145,145,142,0,68,170,273,0,0,0,159,132,132,132,394,138,145,145,128,0,0,0,159,132,388,138,145,0,254,128,128,0,0,0,159,388,138,145,0,254,248,6,254,0,0,0,159,132,388,138,145,0,254,130,254,0,0,0,159,388,138,145,0,130,254,130,254,0,0,0,159,132,388,138,145,0,124,130,124,0,0,0,351,324,324,324,458,330,337,337,320,0,0,0,159,132,132,228,138,138,145,145,128,0,0,0,159,132,228,138,145,0,254,128,128,0,0,0,159,132,228,138,145,128,2,2,254,0,0,0,159,132,228,138,145,0,254,130,254,0,0,0,159,228,138,145,0,130,254,130,254,0,0,0,159,132,228,138,145,0,124,130,124,0,0,0,351,324,324,372,330,330,337,337,320,0,0,0,254,16,40,68,130,16,16,511,0,0,0,0,254,16,40,198,0,511,16,16,16,0,0,0,254,40,198,0,511,16,18,2,254,0,0,0,254,40,198,0,511,16,124,130,124,0,0,0,254,40,198,0,511,0,124,130,124,0,0,0,159,132,132,132,138,138,145,145,128,0,0,0,159,132,132,138,145,0,254,128,128,0,0,0,159,132,132,138,145,128,2,2,254,0,0,0,159,132,138,145,0,254,248,6,254,0,0,0,159,132,132,138,145,128,16,40,198,0,0,0,351,330,330,330,458,341,341,341,320,0,0,0,238,68,170,16,511,0,254,128,128,0,0,0,238,68,170,16,511,16,254,40,198,0,0,0,142,128,159,132,388,138,138,145,128,0,0,0,132,159,388,138,145,0,254,128,128,0,0,0,132,159,388,138,145,254,248,6,254,0,0,0,132,159,388,138,145,0,254,130,254,0,0,0,132,159,388,138,145,0,254,40,198,0,0,0,334,320,351,324,452,330,330,337,320,0,0,0,132,159,228,138,145,0,254,128,128,0,0,0,132,159,228,138,145,254,248,6,254,0,0,0,132,159,228,138,145,130,254,130,254,0,0,0,132,159,228,138,145,128,16,40,198,0,0,0,334,320,351,324,372,330,330,337,320,0,0,0,132,223,132,202,145,0,68,170,273,0,0,0,16,254,40,198,16,511,0,254,128,0,0,0,16,254,40,198,16,511,124,130,124,0,0,0,16,254,16,40,198,0,511,16,16,0,0,0,16,254,108,511,16,254,248,6,254,0,0,0,16,254,40,198,511,16,124,130,124,0,0,0,142,128,159,132,132,138,138,145,128,0,0,0,132,159,132,138,145,128,2,2,254,0,0,0,132,159,132,138,145,254,248,6,254,0,0,0,132,159,132,138,145,0,254,130,254,0,0,0,159,144,240,159,136,232,132,131,128,0,0,0,254,128,254,128,511,0,2,2,254,0,0,0,159,144,144,159,136,136,132,131,128,0,0,0,159,129,415,129,159,0,254,128,128,0,0,0,159,129,415,129,159,128,2,2,254,0,0,0,159,129,415,129,159,254,248,6,254,0,0,0,351,321,479,321,351,0,510,256,256,0,0,0,159,129,129,239,129,129,129,159,128,0,0,0,254,126,2,254,16,511,124,130,124,0,0,0,159,129,159,129,159,132,132,191,128,0,0,0,254,126,2,254,511,0,254,130,254,0,0,0,191,146,146,146,402,146,146,191,128,0,0,0,191,146,402,146,191,128,2,2,254,0,0,0,351,330,330,330,458,330,330,351,320,0,0,0,191,146,146,242,146,146,146,191,128,0,0,0,159,234,138,234,159,128,2,2,254,0,0,0,254,68,68,68,254,16,16,511,0,0,0,0,254,68,254,16,511,0,254,128,128,0,0,0,254,68,68,68,254,68,68,511,0,0,0,0,254,68,254,511,16,254,248,6,254,0,0,0,191,146,146,146,146,146,146,191,128,0,0,0,142,128,191,128,398,145,145,142,128,0,0,0,132,191,398,145,142,128,2,2,254,0,0,0,132,191,398,145,142,254,248,6,254,0,0,0,132,191,398,145,142,0,254,130,254,0,0,0,132,191,398,145,142,130,254,130,254,0,0,0,334,320,351,320,462,337,337,334,320,0,0,0,324,351,462,337,334,0,68,170,273,0,0,0,324,351,462,337,334,0,252,258,252,0,0,0,132,447,142,401,142,0,124,130,124,0,0,0,132,159,238,145,142,0,254,130,254,0,0,0,142,128,159,224,142,241,145,142,128,0,0,0,132,223,142,209,142,128,2,2,254,0,0,0,132,223,142,209,142,0,254,130,254,0,0,0,132,223,142,209,142,130,254,130,254,0,0,0,16,511,0,124,130,124,16,511,0,0,0,0,16,511,130,124,16,511,0,254,128,0,0,0,16,511,130,124,16,511,0,2,254,0,0,0,132,191,128,142,401,142,132,191,128,0,0,0,132,191,402,140,132,191,0,254,128,0,0,0,132,191,402,140,132,255,248,6,254,0,0,0,132,191,402,140,132,191,124,130,124,0,0,0,132,191,128,142,145,142,132,191,128,0,0,0,132,191,146,140,132,191,0,254,128,0,0,0,16,511,124,130,124,0,511,16,16,0,0,0,16,511,130,124,511,0,2,2,254,0,0,0,142,128,191,128,142,145,145,142,128,0,0,0,132,191,142,145,142,128,2,2,254,0]
text_lines: List[List[number]] = [[9],[239,148,249,0,161,72,0,272,207],[96,201,248,0,54,67,101,0,54,288,174,219,187],[65,154,328,89,0,273,189,253,0,54,288,4],[348,229,252,93,6],[215,88,0,77,0,251,224,94,243,0,69,199,339,252],[96,201,249,0,178,160,136,219,0,290,205,230,93,6],[],[2,348,229,4,0,96,201,248,0,254,173,0,54,288,251,0,79,174],[181,271,249,0,261,0,209,56,0,258,278,0,208,192,15,0,237,136],[251,224,94,249,0,101,232,0,273,189,251,0,102,138,249],[245,333,0,204,242,0,274,199,228,6,2],[96,201,248,0,56,158,219,0,179,280,93,6,0,54,288],[201,175,249,0,252,236,328,147,0,102,138,239,104,219,0,308],[101,241,252,0,107,0,194,0,258,93,6,0,328,278,141,0,254,173],[54,288,219,0,252,0,181,202,249,0,209,136,147,0,259,201,251],[278,245,134,0,86,254,0,67,349,35,0,107,278,101],[149,133,93,6],[69,199,339,251,0,272,207,249,0,163,205,111,221],[102,138,239,104,35,35,0,106,93,6],[251,224,94,219,0,341,125,328,89,0,292,328,146,0,254,173],[54,288,251,0,160,271,252,0,106,93,6],[9,5,16],[178,160,0,324,311,0,239,162,0,260,268],[96,201,248,0,251,224,94,219,0,332,131,329,93,6],[69,199,339,248,0,254,173,251,0,200,158,0,315,303],[67,59,249,0,57,51,328,67,0,245,333,0,324,311,249],[54,191,247,127,0,239,162,333,212,0,329,93,56],[190,148,329,93,6],[328,278,141,0,67,286,222,139,93,0,254,173,0,54,288,252],[46,155,328,56,0,258,215,0,324,311,249,0,231,67,67,35],[197,278,0,208,93,6],[96,201,248,0,324,311,249,0,207,268,328,48,0,239,162,330],[166,169,249,0,53,271,333,212,0,329,93,6],[54,288,0,201,175,249,0,252,236,333,0,279,270,0,67,286,127],[324,311,249,0,239,162,329,93,6],[160,194,72,219,48,0,239,162,249,0,145,67,56],[259,201,248,0,54,191,219,187,0,209,136,161,252,134],[346,171,329,93,6],[9,5,17],[160,271,251,0,295,0,256,154],[96,201,248,0,251,224,94,251,0,272,207,249],[163,205,111,252,89,0,292,328,147,187,0,254,173,0,54,288],[183,174,219,0,64,0,181,202,249,0,171,56,329,93,6],[183,174,89,0,96,201,219,48,0,251,224,94,251],[241,279,256,249,0,318,206,333,0,171,56,328,117,56],[278,199,329,93,6],[251,224,94,251,0,260,268,0,55,350,249,0,209,205,80],[96,201,248,0,215,115,0,271,171,134,0,268,95,330,278],[56,158,329,93,6],[251,224,94,251,0,55,350,249,0,181,202,97,127],[268,95,329,93,6],[251,224,94,249,0,171,342,328,67,0,245,333,0,43,282],[271,171,134,0,268,95,329,93,6],[9,5,16,5,16],[251,224,94,0,79,174,251,0,160,271,0,251,343],[96,201,248,0,54,288,0,201,175,249,0,252,236,333],[324,311,249,0,239,162,330,0,275,178,134,0,139,297,93,6],[64,123,100,0,251,224,94,0,79,174,219,187],[69,265,280,252,0,254,173,0,54,288,58,0,151,121],[270,298,329,93,89,0,192,155,252,0,321,280,93,6],[141,213,0,69,265,280,252,0,160,271,252,117,147,0,324,311],[239,162,0,55,350,252,0,164,36,107,0,194,101,0,258,93,6],[328,278,141,0,346,202,329,0,277,43,0,217,252,0,104,130,134],[251,203,328,89,0,47,101,0,245,337,328,93,6],[69,265,280,219,48,0,260,268,0,271,171,134],[268,95,328,278,0,208,89,93,6],[346,202,329,0,277,43,35,0,217,247,92,0,254,94],[278,307,173,93,6],[9,5,16,5,17],[160,194,72,252,0,296,323,105,93],[96,201,248,0,160,194,72,219,48,0,324,311,0,239,162,249],[145,67,56,0,54,191,219,0,78,210,93,6],[64,122,75,0,239,162,0,101,276,0,160,194,72,252,0,254,173],[54,288,251,0,46,155,219,0,45,136,56,0,141,93,6],[324,311,0,239,162,219,0,59,126,106,0,251,224,94,243],[254,174,70,278,0,296,323,105,218,93,89,0,192,200,252],[111,124,230,93,6],[254,173,0,54,288,248,0,96,201,219,48,101,0,181,44,219],[59,333,0,281,155,328,67,0,199,260,329,93,6],[259,201,58,0,59,55,217,89,0,254,252,117,56],[274,264,329,93,6],[54,288,0,201,175,249,0,252,236,333,0,296,323,106],[251,224,94,243,111,249,0,326,215,275,93,6],[9,5,17,5,16],[254,173,0,54,288,251,0,201,129],[96,201,252,0,268,95,329,0,271,171,127,0,251,224,94,243],[254,174,35,0,296,323,105,218,93,6],[254,173,0,54,288,0,183,174,89,0,96,201,251,0,90,125,249],[253,271,328,56,0,98,238,0,201,129,328,67],[199,260,329,93,6],[328,278,141,0,104,130,111,252,0,296,323,105,218,93,89],[192,200,249,0,111,248,0,96,201,248,0,139,250,252],[352,111,137,93,6],[252,272,0,254,173,0,54,288,251,0,201,129,134,0,252,236,333],[102,138,239,104,249,0,101,240,0,194,101,0,258,56,4],[233,268,353,0,254,173,0,54,288,251,0,322,219,0,190],[194,101,0,258,93,6],[254,173,0,54,288,251,0,201,129,134,0,252,236,333],[102,138,239,104,249,0,103,89,93,6],[102,138,239,104,249,0,323,67,328,56,0,254,173],[54,288,219,0,302,191,329,93,6],[9,5,17,5,17],[43,282,0,171,56,35,0,164,36,105,93],[96,201,248,0,251,224,94,249,0,171,342,328,67,0,245,333],[254,173,0,54,288,219,0,43,282,0,271,171,134],[268,95,334,93,6],[328,278,141,0,254,173,0,54,288,248,0,93,133,0,54,127,127],[257,194,329,0,271,171,232,0,96,201,251,0,171,56,35],[93,132,93,89,0,181,202,249,0,164,52,329,93,6],[183,174,89,0,96,201,249,0,176,122,0,203,155,329,93,6],[2,348,229,1,0,84,35,0,237,136,134,0,193,225,93,89],[277,43,35,0,75,234,93,1,2],[53,62,0,96,201,248,0,254,173,0,54,288,249,0,193,253],[340,251,127,0,296,323,105,215,0,40,229,219,0,38,354,93,6],[9,5,16,5,16,5,16],[176,201,247,127,0,154,82,280,0,260,268],[96,201,248,0,69,265,280,219,48,0,260,268,0,271,171,134],[268,95,328,278,0,208,67,127,0,334,93,6],[328,278,141,0,69,265,280,248,0,259,201,249],[251,203,328,89,0,96,201,219,48,0,41,328,48],[162,164,329,93,6],[251,224,94,0,79,174,219,187,89,0,187,127,134],[251,203,328,89,0,175,245,67,35,0,321,278,67],[53,62,0,79,174,0,39,112,247,127,0,260,268,0,275,178,35],[278,223,105,56,4,0,254,173,0,54,288,251,0,40,199,70,278],[41,345,106,93,6],[324,311,0,239,162,0,55,350,248,0,202,335,105,278,0,153,329],[291,0,202,320,127,0,74,76,93,6],[9,5,16,5,16,5,17],[69,265,280,251,0,167,201],[96,201,248,0,346,202,329,0,277,43,35,0,217,93,89],[252,246,127,0,69,265,280,249,0,278,307,171,67,127],[334,93,6],[64,122,75,0,146,305,0,109,0,254,173,0,54,288,252],[324,311,0,239,162,0,264,192,134,0,66,198,329,93,6],[69,265,280,249,0,315,333,0,251,224,94,251,0,271,171,35],[254,173,0,54,288,219,0,268,95,105,218,99,0,47,252,93,6],[96,201,248,0,339,264,219,187,0,296,323,105,215],[203,155,202,127,0,73,124,37,93,6],[254,173,0,54,288,0,37,174,35,0,156,89,93,6],[2,348,229,4,0,54,288,253,0,84,35,0,215,283,187],[251,224,94,58,0,331,71,0,258,218,88,81,15,2],[252,272,0,96,201,248,0,259,201,251,0,271,296,134],[190,148,333,212,0,329,93,6],[2,75,89,0,251,224,94,219,0,160,271,247,127,0,262,257,329],[47,252,93,1,2],[2,75,89,0,273,189,251,0,102,138,249,0,245,333],[204,244,93,1,2],[9,5,16,5,17,5,16],[87,61,219,48,101,0,201,129,163,278,0,153,328,93],[96,201,248,0,296,323,106,0,251,224,94,243,111,58],[59,55,35,0,217,93,56,0,274,264,334,93,6],[328,278,141,0,254,173,0,54,288,248,0,96,201,252],[251,224,94,58,0,270,298,334,93,89,0,181,202,249],[209,205,80,93,6],[329,322,0,251,224,94,248,0,96,201,252,0,104,130,111,249],[168,136,56,0,344,259,0,182,205,78,247,124,0,334,93,56],[186,36,329,93,6],[53,62,0,254,173,0,54,288,58,0,251,224,94,0,214,284],[149,108,251,0,251,203,249,0,163,48,0,106,93,6],[96,201,248,0,254,173,0,54,288,219,0,296,323,105,215],[40,229,219,0,38,354,93,6],[9,5,16,5,17,5,17],[324,311,0,239,162,0,191,57],[296,323,106,0,251,224,94,243,111,249],[326,215,274,218,93,6],[254,173,0,54,288,248,0,96,201,251,0,190,148,249],[251,203,334,278,141,4,0,42,248,0,54,288,252,117,89],[252,246,127,0,254,94,0,159,215,0,274,218,93,6],[326,124,76,0,251,224,94,243,111,248,0,324,311,249],[93,199,0,239,162,328,67,0,199,260,329,93,6],[146,305,0,109,0,324,311,252,0,154,181,353,0,54,191,219],[101,287,334,93,89,0,223,118,252,0,230,93,6],[252,272,0,57,51,330,0,264,192,134,0,53,271,333,212],[329,93,6],[254,173,0,200,158,0,315,303,251,0,276,203,253],[273,189,299,102,174,134,0,57,51,329,93,6],[254,173,0,54,288,251,0,274,235,0,199,190,249],[57,51,329,93,6],[9,5,16,5,16,5,17,5,16],[160,271,252,117,89,0,274,264],[96,201,248,0,254,173,0,54,288,0,37,174,219,48],[259,201,252,0,251,224,94,219,0,160,271,247,127],[262,257,334,93,56,0,274,264,329,93,6],[2,266,89,0,251,224,94,251,0,271,171,134,0,216,67],[245,333,0,254,174,122,0,64,111,58,0,331,71],[335,104,334,198,92,93,1,2],[254,173,0,54,288,248,0,96,201,251,0,58,43,0,67,128,249],[273,181,328,67,0,199,260,329,93,6],[273,44,0,319,271,14,0,252,268,219,0,160,271,247,127],[347,104,329,0,67,128,252,0,258,89,35,15],[29,21,19,27,29,20,5,34,21,30],[160,271,0,252,125,0,253,271],[254,173,0,54,288,248,0,96,201,252,0,252,268,219],[251,224,94,251,0,271,171,134,0,272,57,334,99],[67,128,249,0,164,52,329,93,6],[96,201,251,0,274,264,249,0,163,205,111,253,0,183,174,89],[96,201,249,0,188,166,329,93,6],[96,201,248,0,254,173,0,54,288,251,0,201,129,134],[216,218,278,141,4,0,273,189,251,0,102,138,249,0,245,333],[204,237,99,0,181,120,111,219,48,89,0,167,201,259,127],[78,48,0,106,93,6],[29,21,19,27,29,20,5,26,27],[160,271,0,252,125,0,176,253,271],[254,173,0,54,288,248,0,96,201,251,0,274,264,249],[110,163,306,330,0,67,128,249,0,290,278,0,153,329,93,6],[2,43,282,143,328,278,0,139,117,1,0,84,35],[251,224,94,249,0,101,234,93,89,0,277,43,89],[302,175,328,93,1,2],[53,62,0,96,201,248,0,251,224,94,219,0,341,125,329],[340,251,127,0,40,229,219,0,38,354,93,6],[9,5,16,5,16,5,17,5,17],[102,138,239,104,35,251,0,53,203],[96,201,248,0,254,173,0,54,288,251,0,203,155],[211,219,187,101,0,259,201,251,0,116,249,0,63,353,278],[208,89,93,6],[335,104,334,93,6,0,351,349,328,278,0,208,89,93,1,2],[254,173,0,54,288,248,0,96,201,219,48,0,251,224,94,251],[271,171,134,0,165,353,117,56,0,41,235,329,93,6],[328,278,141,0,96,201,248,0,74,79,0,104,130,111,251],[252,135,249,0,143,328,278,0,208,89,93,6],[53,62,0,96,201,248,0,102,138,239,104,219,0,289,221,329],[9,5,16,5,17,5,17,5,16],[273,189,299,102,174,0,57,51],[96,201,58,0,251,224,94,248,0,273,189,299,102,174,134],[57,51,328,67,127,0,53,271,329,93,6],[293,266,329,0,275,178,0,74,219,0,324,311,249,0,150,325],[278,269,70,278,0,239,162,328,89,0,100,0,191,57,329,93,6],[328,278,141,0,139,278,140,0,195,37,70,278,0,68,264,249],[91,301,0,194,0,217,93,6],[252,272,0,260,268,251,0,191,57,0,221,174,35],[53,271,106,93,6],[13,8,3,0,324,311,0,324,164,0,191,57,0,7,0,10,8,3,0,324,311],[176,164],[23,27,33,5,30,32,19,19,21,30,30],[273,189,299,102,174,0,260,268,0,191,57],[60,250,58,0,331,71,0,324,311,252,0,324,164,329,93,6],[251,224,94,251,0,260,268,252,0,191,57,334,93,89],[192,200,252,0,54,191,219,0,321,280,93,6],[96,201,58,0,104,130,111,248,0,254,173,0,54,288,251],[300,267,249,0,327,333,0,152,249,0,196,68,93,6],[23,27,33,5,22,18,24,25],[273,189,299,102,174,0,260,268,0,176,164],[324,311,252,0,314,278,278,0,208,210,93,1],[254,173,0,54,288,248,0,339,264,219,187,0,324,311,249],[164,52,328,56,0,274,170,249,0,194,185,329,93,6],[96,201,248,0,312,301,249,0,199,101,328,278,141,0,53,62],[296,323,105,215,0,40,229,219,0,38,354,93,6],[9,5,16,5,17,5,17,5,17],[254,173,0,54,288,0,199,190,0,57,51],[96,201,58,0,251,224,94,248,0,254,173,0,54,288,251],[274,235,0,199,190,249,0,57,51,328,67,127],[53,271,329,93,6],[54,288,0,79,174,0,181,271,249,0,261,0,205,89],[96,201,248,0,104,130,111,219,48,0,199,190,251,0,54,178],[183,348,249,0,209,124,275,93,6],[251,224,94,248,0,55,350,219,0,114,117,0,324,311,249],[239,162,328,278,141,4,0,254,173,0,54,288,251,0,195,288,252],[227,183,171,93,0,180,136,0,199,260,106,93,6],[58,223,0,260,268,248,0,191,57,330,0,194,0,258,249,70,15],[28,27,25,24,19,21,5,30,32,19,19,21,30,30],[54,288,0,199,190,0,260,268,0,191,57],[251,224,94,252,0,190,303,329,0,324,311,252],[191,57,267,247,127,0,324,164,329,93,6],[254,173,0,54,288,248,0,308,0,344,119,219,0,179,278,56,4],[96,201,58,0,104,130,111,248,0,64,0,317,249,0,252,236,333],[312,301,329,93,6],[245,337,329,0,260,268,252,218,278,141,0,150,325,134],[95,191,334,93,6],[28,27,25,24,19,21,5,22,18,24,25],[54,288,0,199,190,0,260,268,0,176,164],[324,311,252,0,260,104,328,278,0,208,89,93,6],[195,288,0,276,252,99,0,254,173,0,54,288,252,0,194,183,329],[241,279,256,249,0,164,52,328,56,0,54,171,134],[240,137,93,6],[96,201,248,0,101,144,303,124,0,328,278,141],[54,288,219,48,0,177,263,338,0,40,229,219,0,38,354,93,6],[9,5,17,5,16,5,16],[245,337,329,0,252,276,294,259],[96,201,248,0,254,173,0,54,288,251,0,201,129,134,0,216,248],[109,0,93,199,0,251,224,94,249,0,103,67,127],[53,203,329,93,6],[64,122,75,0,251,224,94,248,0,252,157,0,96,201,252],[271,171,134,0,83,50,0,104,130,111,252],[296,323,105,218,93,89,0,181,202,249,0,209,56,0,258,93,6],[69,199,339,252,0,286,35,239,0,325,271,247,127],[156,89,93,6],[2,348,229,4,0,237,136,35,0,96,201,249,0,93,199],[159,215,101,0,105,49,192,15,2],[96,201,248,0,259,201,251,0,335,104,249,0,351,349,328,146],[93,199,0,67,349,134,0,95,117,56,0,174,310,329,93,6],[12,8,3,0,201,129,0,349,172,0,7,0,11,8,3,0,201,129],[349,172,0,202,320],[31,29,32,30,31,5,34,21,30],[201,129,0,349,172],[251,224,94,248,0,96,201,219,48,0,139,278,140],[67,349,134,0,275,93,6],[96,201,248,0,93,199,0,251,224,94,219,0,332,131,328,221],[324,311,0,239,162,0,260,268,249,0,275,178,329,93,6],[9,5,16,6,0,178,160,0,324,311,0,239,162,0,260,268,247,127],[252,104,332,92,93,6],[31,29,32,30,31,5,26,27],[201,129,0,349,172,0,202,320],[251,224,94,248,0,96,201,251,0,167,201,249],[236,187,328,278,0,208,89,93,6],[53,62,0,96,201,248,0,273,279,219,187,0,285,50,75,56],[102,138,239,104,219,0,93,199,0,289,221,330,0,67,349,134],[255,89,93,6],[9,5,17,5,16,5,17],[167,201,259,251,0,143,127],[96,201,248,0,254,173,0,54,288,219,0,55,193],[302,191,328,67,127,0,53,271,329,93,6],[251,224,94,251,0,271,171,134,0,83,67,89,0,254,252],[162,172,105,147,187,0,98,0,142,248],[102,138,239,104,35,35,0,245,337,219,0,179,280,93,6],[53,62,0,251,224,94,248,0,96,201,252,0,254,173],[54,288,251,0,160,271,252,117,89,0,181,202,249],[69,199,339,248,0,175,85,328,146,0,143,329,93,6],[2,237,136,89,0,96,201,249,0,104,278,117,56],[159,218,192,6,0,328,278,141,0,96,201,248,0,237,136,134],[167,201,334,192,1,2],[96,201,248,0,251,224,94,219,187,0,226,243,353],[300,166,106,93,6],[16,0,93,250,0,0,17,0,252,268],[166,336,309,14,0,16,7,17,0,189,313],[16],[17],[16,0,346,271,0,0,17,0,173,155],[252,212,67,251,0,74],[96,201,251,0,189,313,252,0,78,210,198,92,93,6],[16,0,184,0,48,256],[17,0,127,178,127],[40,229,0,220,113],[260,268,0,202,320,0,220,113],[304,254,318,0,220,113],[191,57,0,220,113],[316,301,0,220,113]]
node_ids: List[number] = [0,22,39,54,69,84,102,115,129,149,163,180,192,203,212,223,235,242,249,261,270,278,294,302,309]
node_titles: List[number] = [1,23,40,55,70,85,103,116,130,150,164,181,193,204,213,224,236,243,250,262,271,279,295,303,310]
node_art: List[number] = [0,1,2,3,4,5,6,7,6,8,9,10,5,11,12,13,15,16,14,15,16,17,18,19,20]
node_kind: List[number] = [0,0,0,0,0,0,5,6,0,5,0,1,7,5,5,2,8,5,2,8,5,3,4,9,9]
page_starts: List[number] = [0,18,33,42,54,66,81,96,111,132,147,162,174,186,195,210,225,231,240,255,264,273,291,300,306]
page_lengths: List[number] = [18,15,9,12,12,15,15,15,21,15,15,12,12,9,15,15,6,9,15,9,9,18,9,6,18]
page_counts: List[number] = [6,5,3,4,4,5,5,5,7,5,5,4,4,3,5,5,2,3,5,3,3,6,3,2,6]
body_lines: List[number] = [2,3,4,5,6,7,8,9,10,11,7,7,12,13,14,15,16,17,24,7,7,25,26,27,28,7,7,29,30,31,32,33,7,41,42,43,44,45,46,47,48,49,56,57,7,58,59,60,61,62,7,63,64,7,71,72,7,73,74,7,75,76,77,78,79,7,86,87,7,88,89,90,91,92,93,94,95,96,97,7,7,104,105,106,107,108,109,110,7,7,111,112,7,113,114,7,117,118,7,119,120,121,122,123,90,124,125,126,127,128,7,131,132,133,134,135,7,136,137,7,138,139,7,140,7,7,141,142,7,143,144,7,151,152,7,153,154,155,156,157,158,159,160,7,161,162,7,56,165,166,167,168,169,170,171,7,172,173,7,174,175,7,182,183,184,185,186,187,188,189,7,190,191,7,194,195,196,197,198,7,199,200,201,202,7,7,205,206,7,207,208,209,210,211,7,214,215,216,147,217,7,218,219,7,220,221,7,222,211,7,225,226,7,227,228,7,229,230,7,231,232,7,233,234,7,237,238,239,240,241,7,244,7,7,245,246,7,247,248,7,251,252,253,254,255,256,257,258,259,260,7,7,233,234,7,263,264,7,265,266,267,268,269,7,272,7,7,273,274,275,276,277,7,280,281,282,283,284,285,286,287,7,288,289,7,290,291,7,292,293,7,296,297,7,298,299,7,300,301,7,304,305,7,306,307,308,311,312,7,313,314,315,316,317,155,318,7,7,319,320,321,322,323,7]
choice_starts: List[number] = [0,2,4,6,9,11,13,15,17,19,21,23,25,25,25,25,25,27,29,29,29,31,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33]
choice_lengths: List[number] = [2,2,2,3,2,2,2,2,2,2,2,2,0,0,0,0,2,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
choice_lines: List[number] = [18,19,20,21,34,35,36,37,38,50,51,52,53,65,66,67,68,80,81,82,83,98,99,100,101,145,146,147,148,176,177,178,179]
choice_icons: List[number] = [0,1,2,3,4,5,6,7,8,9,10,11,0,1,0,1,12,13,0,1,14,15,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
next_a: List[number] = [1,3,5,7,9,21,-1,-1,11,-1,15,12,-1,-1,-1,16,-1,-1,19,-1,-1,22,1,-1,-1]
next_b: List[number] = [2,4,6,8,10,24,-1,-1,14,-1,18,13,-1,-1,-1,17,-1,-1,20,-1,-1,23,-1,-1,-1]
ending_titles: List[number] = [7,7,7,7,7,333,334,335,336,337]
ending_art: List[number] = [0,0,0,0,0,11,21,23,22,19]
HELP_NEXT = 324
HELP_PICK = 325
LETTER_A = 326
LETTER_B = 327
HELP_CONFIRM = 328
ENDING_LABEL = 329
ENDING_NOTE = 330
ENDING_RESTART = 331
ENDING_LOBBY = 332
RECORD_NODE = 5
# MakeCode Arcade Python runtime; all text is encoded bitmap data.
canvas = scene.background_image()
mode = 0
current_node = 0
page_index = 0
selected_option = 0
spy_record = False
blink = False

def ink(line_id: number, x: number, y: number, color: number):
    for glyph in text_lines[line_id]:
        for row in range(12):
            bits = font_bits[glyph * 12 + row]
            for col in range(font_width[glyph]):
                if (bits & (1 << col)) != 0:
                    canvas.set_pixel(x + col, y + row, color)
        x += font_width[glyph]

def person(x: number, y: number, coat: number, police_hat: bool):
    canvas.fill_rect(x + 4, y, 8, 3, 15)
    canvas.fill_rect(x + 3, y + 3, 10, 8, 13)
    canvas.set_pixel(x + 5, y + 6, 15)
    canvas.set_pixel(x + 10, y + 6, 15)
    canvas.fill_rect(x + 6, y + 11, 4, 2, 13)
    canvas.fill_rect(x + 2, y + 13, 12, 12, coat)
    canvas.fill_rect(x, y + 14, 2, 10, coat)
    canvas.fill_rect(x + 14, y + 14, 2, 10, coat)
    canvas.fill_rect(x + 3, y + 25, 4, 5, 15)
    canvas.fill_rect(x + 9, y + 25, 4, 5, 15)
    if police_hat:
        canvas.fill_rect(x + 2, y - 2, 12, 4, 8)
        canvas.fill_rect(x + 1, y + 2, 14, 2, 15)
        canvas.fill_rect(x + 7, y, 2, 2, 5)
    else:
        canvas.fill_rect(x + 3, y, 10, 3, 15)

def paper(x: number, y: number):
    canvas.fill_rect(x, y, 16, 21, 13)
    canvas.draw_rect(x, y, 16, 21, 14)
    for r in range(4):
        canvas.fill_rect(x + 3, y + 4 + r * 4, 10, 1, 12)

def crate(x: number, y: number):
    canvas.fill_rect(x, y, 20, 15, 14)
    canvas.draw_rect(x, y, 20, 15, 13)
    canvas.draw_line(x, y, x + 19, y + 14, 13)
    canvas.draw_line(x + 19, y, x, y + 14, 13)

def emblem(kind: number, x: number, y: number):
    # 20 x 20 selectable pictograms, native pixel graphics.
    if kind == 0 or kind == 10 or kind == 13:
        canvas.fill_rect(x + 2, y + 1, 2, 19, 13)
        canvas.fill_rect(x + 4, y + 2, 15, 10, 1)
        canvas.fill_rect(x + 9, y + 4, 5, 3, 2)
        canvas.fill_rect(x + 9, y + 7, 5, 3, 8)
    elif kind == 1 or kind == 4 or kind == 5:
        paper(x + 2, y)
        if kind == 5:
            canvas.draw_line(x + 4, y + 4, x + 16, y + 16, 2)
            canvas.draw_line(x + 16, y + 4, x + 4, y + 16, 2)
        elif kind == 4:
            canvas.draw_line(x + 4, y + 12, x + 8, y + 16, 7)
            canvas.draw_line(x + 8, y + 16, x + 16, y + 7, 7)
    elif kind == 2:
        canvas.fill_rect(x + 2, y + 5, 17, 11, 8)
        canvas.fill_rect(x + 3, y + 1, 10, 7, 8)
        canvas.fill_rect(x + 5, y + 3, 5, 4, 9)
        canvas.fill_rect(x + 15, y + 1, 3, 6, 15)
        canvas.fill_rect(x + 3, y + 16, 4, 4, 15)
        canvas.fill_rect(x + 13, y + 16, 4, 4, 15)
    elif kind == 3:
        crate(x, y + 4)
    elif kind == 6:
        canvas.draw_rect(x + 6, y + 1, 9, 10, 13)
        canvas.fill_rect(x + 3, y + 8, 15, 12, 5)
        canvas.fill_rect(x + 9, y + 12, 3, 5, 15)
    elif kind == 7:
        canvas.fill_rect(x + 2, y + 7, 17, 7, 1)
        canvas.fill_rect(x + 5, y + 4, 11, 13, 1)
        canvas.fill_rect(x + 8, y + 6, 6, 9, 8)
        canvas.fill_rect(x + 10, y + 8, 2, 5, 15)
    elif kind == 8:
        canvas.draw_line(x + 3, y + 3, x + 17, y + 17, 2)
        canvas.draw_line(x + 17, y + 3, x + 3, y + 17, 2)
        canvas.draw_rect(x + 1, y + 1, 19, 19, 2)
    elif kind == 9:
        canvas.draw_rect(x + 1, y + 2, 9, 9, 5)
        canvas.fill_rect(x + 8, y + 9, 10, 3, 5)
        canvas.fill_rect(x + 13, y + 10, 3, 6, 5)
        canvas.fill_rect(x + 17, y + 10, 3, 5, 5)
    elif kind == 11:
        canvas.fill_rect(x + 4, y + 1, 13, 13, 8)
        canvas.fill_rect(x + 7, y + 14, 7, 4, 8)
        canvas.fill_rect(x + 9, y + 4, 3, 8, 5)
        canvas.fill_rect(x + 6, y + 6, 9, 3, 5)
    elif kind == 12:
        canvas.fill_rect(x + 2, y + 5, 17, 12, 15)
        canvas.fill_rect(x + 4, y + 8, 4, 3, 1)
        canvas.fill_rect(x + 13, y + 8, 4, 3, 1)
    else:
        canvas.fill_rect(x + 1, y + 7, 19, 12, 11)
        canvas.fill_rect(x + 4, y + 4, 13, 4, 13)
        if kind == 14:
            canvas.fill_rect(x + 7, y + 1, 7, 4, 13)
        else:
            canvas.fill_rect(x + 8, y + 1, 5, 5, 8)
        for r in range(3):
            canvas.fill_rect(x + 3 + r * 6, y + 10, 3, 4, 9)
        canvas.fill_rect(x + 8, y + 15, 5, 5, 15)

def art(kind: number):
    # Scene strip is y=29..65; every story node uses its own composition.
    canvas.fill_rect(2, 29, 156, 37, 12)
    canvas.fill_rect(2, 59, 156, 7, 14)
    canvas.fill_rect(133, 32, 8, 8, 13)
    if kind == 0: # secret meeting
        canvas.fill_rect(12, 32, 24, 25, 15)
        canvas.draw_rect(15, 35, 18, 19, 6)
        person(43, 34, 8, True)
        person(100, 34, 14, False)
        canvas.fill_rect(67, 51, 24, 3, 13)
        canvas.fill_rect(70, 54, 3, 11, 15)
        paper(72, 30)
    elif kind == 1: # train
        canvas.draw_line(5, 63, 155, 63, 11)
        canvas.fill_rect(10, 43, 71, 16, 8)
        for r in range(5):
            canvas.fill_rect(15 + r * 13, 46, 8, 6, 9)
        canvas.fill_rect(83, 38, 24, 21, 8)
        canvas.fill_rect(108, 46, 20, 13, 8)
        canvas.fill_rect(116, 34, 6, 12, 15)
        for r in range(6):
            canvas.fill_rect(17 + r * 19, 58, 7, 5, 15)
        crate(133, 48)
    elif kind == 2 or kind == 3: # report / secret contact
        person(28, 34, 8 if kind == 2 else 14, kind == 2)
        person(116, 34, 8, True)
        paper(73, 34)
        if kind == 3:
            canvas.fill_rect(61, 29, 4, 37, 15)
            canvas.draw_line(52, 41, 69, 41, 2)
    elif kind == 4: # arrest
        person(29, 34, 8, True)
        person(66, 34, 14, False)
        person(111, 34, 8, True)
        crate(8, 50)
        canvas.draw_line(41, 55, 69, 55, 11)
        canvas.draw_line(79, 55, 114, 55, 11)
    elif kind == 5: # badge / trust by police
        person(37, 34, 8, True)
        emblem(11, 73, 38)
        paper(111, 34)
    elif kind == 6: # interrogation
        person(36, 34, 14, False)
        person(112, 34, 8, True)
        canvas.fill_rect(58, 52, 45, 4, 13)
        canvas.fill_rect(65, 56, 3, 10, 15)
        canvas.fill_rect(94, 56, 3, 10, 15)
        canvas.draw_line(80, 29, 80, 35, 15)
        canvas.fill_rect(74, 35, 13, 3, 5)
    elif kind == 7: # conflict
        person(34, 34, 14, False)
        person(106, 34, 6, False)
        emblem(8, 71, 36)
        crate(6, 50)
    elif kind == 8: # alone
        person(73, 34, 8, True)
        canvas.draw_line(40, 38, 29, 52, 2)
        canvas.draw_line(29, 38, 40, 52, 2)
        canvas.draw_line(119, 38, 130, 52, 2)
        canvas.draw_line(130, 38, 119, 52, 2)
    elif kind == 9: # release
        canvas.draw_rect(10, 31, 31, 34, 11)
        for r in range(3):
            canvas.fill_rect(12 + r * 9, 32, 2, 32, 11)
        person(70, 34, 14, False)
        person(117, 34, 8, True)
        emblem(9, 94, 37)
        crate(43, 50)
    elif kind == 10: # record check
        paper(38, 34)
        paper(71, 36)
        paper(103, 34)
        canvas.draw_rect(30, 30, 98, 35, 11)
    elif kind == 11: # prison
        person(72, 34, 11, False)
        canvas.fill_rect(20, 30, 120, 3, 15)
        for r in range(9):
            canvas.fill_rect(22 + r * 14, 31, 3, 35, 11)
        canvas.fill_rect(20, 62, 120, 3, 15)
    elif kind == 12: # resolve
        person(72, 34, 14, False)
        emblem(0, 111, 36)
        canvas.fill_rect(30, 29, 3, 37, 11)
        canvas.fill_rect(48, 29, 3, 37, 11)
    elif kind == 13 or kind == 14: # target buildings (non-operational illustration)
        canvas.fill_rect(33, 43, 95, 22, 11)
        canvas.fill_rect(47, 37, 68, 7, 13)
        canvas.fill_rect(63, 32, 35, 5, 13 if kind == 13 else 8)
        for r in range(7):
            canvas.fill_rect(39 + r * 13, 47, 7, 7, 9)
        canvas.fill_rect(72, 55, 17, 11, 15)
        if kind == 13:
            for r in range(4):
                canvas.fill_rect(49 + r * 18, 55, 3, 10, 13)
        else:
            emblem(11, 8, 38)
    elif kind == 15: # stylized success flash
        canvas.fill_rect(47, 40, 68, 19, 4)
        canvas.fill_rect(62, 30, 37, 35, 4)
        canvas.fill_rect(56, 45, 49, 10, 5)
        canvas.fill_rect(72, 36, 17, 26, 5)
        canvas.fill_rect(76, 42, 9, 13, 1)
        canvas.draw_line(18, 35, 36, 42, 5)
        canvas.draw_line(125, 49, 146, 57, 5)
    elif kind == 16: # dud
        crate(68, 49)
        emblem(8, 69, 29)
        person(119, 34, 8, True)
    elif kind == 17: # request second chance
        person(35, 34, 8, True)
        person(108, 34, 14, False)
        emblem(1, 71, 36)
        canvas.draw_rect(68, 32, 26, 29, 2)
    elif kind == 18: # restored trust
        person(49, 34, 8, True)
        person(94, 34, 14, False)
        canvas.fill_rect(63, 52, 34, 4, 13)
        canvas.draw_line(70, 37, 78, 43, 7)
        canvas.draw_line(78, 43, 90, 32, 7)
    elif kind == 19 or kind == 20: # exile / betrayal
        canvas.draw_rect(16, 30, 36, 36, 15)
        canvas.draw_line(50, 31, 60, 36, 13)
        canvas.draw_line(60, 36, 60, 65, 13)
        person(109, 34, 8, True)
        canvas.draw_line(73, 48, 96, 48, 13)
        canvas.draw_line(90, 43, 96, 48, 13)
        canvas.draw_line(90, 53, 96, 48, 13)
        if kind == 20:
            emblem(8, 20, 38)
    elif kind == 21: # failed plan
        crate(34, 48)
        paper(72, 34)
        emblem(8, 106, 37)
    elif kind == 22: # success ending
        person(45, 34, 14, False)
        person(100, 34, 6, False)
        emblem(0, 73, 34)
        canvas.set_pixel(20, 38, 5)
        canvas.set_pixel(136, 48, 5)
    else: # collaboration ending
        person(70, 34, 8, True)
        emblem(11, 109, 36)
        canvas.fill_rect(27, 35, 20, 22, 15)

def show_title():
    global mode
    mode = 0
    canvas.draw_image(title_image, 0, 0)

def enter_node(node: number):
    global current_node, page_index, selected_option, mode, spy_record
    current_node = node
    page_index = 0
    selected_option = 0
    mode = 1
    if node == RECORD_NODE:
        spy_record = True
    render()

def start_game():
    global spy_record
    spy_record = False
    enter_node(0)

def render():
    canvas.fill(15)
    if mode == 0:
        canvas.draw_image(title_image, 0, 0)
    elif mode == 1:
        ink(node_ids[current_node], 5, 0, 6)
        ink(node_titles[current_node], 5, 13, 5)
        art(node_art[current_node])
        canvas.draw_rect(2, 67, 156, 40, 12)
        first: number = page_starts[current_node] + page_index * 3
        for r in range(3):
            offset: number = page_index * 3 + r
            if offset < page_lengths[current_node]:
                ink(body_lines[first + r], 6, 67 + r * 13, 1)
        ink(HELP_NEXT, 5, 108, 13)
        canvas.fill_rect(118, 114, 36, 2, 12)
        canvas.fill_rect(118, 114, (page_index + 1) * 36 // page_counts[current_node], 2, 6)
    elif mode == 2:
        ink(node_titles[current_node], 5, 0, 5)
        ink(HELP_PICK, 5, 13, 13)
        for option in range(2):
            x = 28 + option * 80
            canvas.draw_rect(x - 7, 29, 35, 27, 5 if option == selected_option else 12)
            emblem(choice_icons[current_node * 2 + option], x, 32)
            ink(LETTER_A if option == 0 else LETTER_B, x - 19, 36, 5 if option == selected_option else 11)
        canvas.draw_rect(2, 59, 156, 48, 12)
        pick = current_node * 2 + selected_option
        for r in range(choice_lengths[pick]):
            ink(choice_lines[choice_starts[pick] + r], 6, 59 + r * 12, 1)
        ink(HELP_CONFIRM, 5, 108, 13)
    else:
        kind = node_kind[current_node]
        ink(ENDING_LABEL, 5, 0, 6)
        ink(ending_titles[kind], 5, 13, 5)
        art(ending_art[kind])
        ink(ENDING_NOTE, 5, 72, 1)
        ink(ENDING_RESTART, 5, 89, 13)
        ink(ENDING_LOBBY, 5, 104, 13)

def finish_node():
    global mode, selected_option
    kind = node_kind[current_node]
    if kind == 0:
        mode = 2
        selected_option = 0
        render()
    elif kind == 1:
        if spy_record:
            enter_node(next_a[current_node])
        else:
            enter_node(next_b[current_node])
    elif kind == 2 or kind == 3:
        threshold = 70 if kind == 2 else 60
        # randint includes both ends: exactly 70/100 or 60/100 outcomes.
        roll = randint(1, 100)
        if roll <= threshold:
            enter_node(next_a[current_node])
        else:
            enter_node(next_b[current_node])
    elif kind == 4:
        # The trust-recovery node returns to 1-A and retains spy_record.
        enter_node(next_a[current_node])
    else:
        mode = 3
        render()

def on_a_pressed():
    global page_index
    if mode == 0 or mode == 3:
        start_game()
    elif mode == 1:
        if page_index + 1 < page_counts[current_node]:
            page_index += 1
            render()
        else:
            finish_node()
    elif mode == 2:
        if selected_option == 0:
            enter_node(next_a[current_node])
        else:
            enter_node(next_b[current_node])

def on_b_pressed():
    global page_index, mode
    if mode == 1 and page_index > 0:
        page_index -= 1
        render()
    elif mode == 2:
        mode = 1
        render()
    elif mode == 3:
        show_title()

def on_arrow_pressed():
    global selected_option
    if mode == 2:
        selected_option = 1 - selected_option
        render()

def animate_title():
    global blink
    if mode == 0:
        blink = not blink
        canvas.draw_rect(29, 80, 102, 26, 5 if blink else 14)

controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_arrow_pressed)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_arrow_pressed)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_arrow_pressed)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_arrow_pressed)
game.on_update_interval(700, animate_title)
show_title()


# --- 편집용 원문 대조표 (표시 데이터는 위 text_lines에 포함) ---
# 1 | 운명을 바꾼 제안 | choice
# 당신은 경기도 경찰부에서 근무하는 조선인 경찰, 황옥이다.
# 어느 날 의열단원 김시현이 당신을 비밀리에 찾아온다.
# "황옥, 당신은 일본 경찰의 내부 사정을 잘 알고 있지 않소? 우리 의열단을 도와 조선의 독립을 위해 싸워 주시오."
# 당신은 고민에 빠진다. 경찰 신분을 이용하면 독립운동에 큰 도움이 될 수 있다. 하지만 일본 경찰에 이 사실을 알리면 자신의 지위를 높일 기회가 될지도 모른다.
# A. 김시현의 제안을 받아들여 독립운동가가 된다. -> 1-A
# B. 의열단에 협력하는 척하며 일본 경찰의 밀정이 된다. -> 1-B
# 1-A | 비밀 폭탄 운반 작전 | choice
# 당신은 의열단에 합류한다.
# 김시현은 일본의 식민 통치 기관을 공격하기 위해 폭탄을 경성으로 운반해야 한다고 설명한다.
# 하지만 기차역마다 일본 경찰이 검문하고 있어 폭탄을 옮기기가 쉽지 않다.
# 당신은 폭탄을 안전하게 운반할 방법을 결정해야 한다.
# A. 경찰 신분을 이용해 직접 기차로 폭탄을 운반한다. -> 1-A-A
# B. 밀수꾼에게 운반을 맡기고 자신은 경성에서 알리바이를 확보한다. -> 1-A-B
# 1-B | 밀정의 첫 임무 | choice
# 당신은 의열단의 제안을 받아들이는 척하면서 일본 경찰 상부에 그 사실을 보고한다.
# 상부는 당신에게 의열단의 움직임을 파악해 보고하라고 지시한다.
# 의열단의 작전 계획을 알아낸 당신은 어떤 정보를 전달할지 고민한다.
# A. 의열단의 계획을 사실대로 전달한다. -> 1-B-A
# B. 의열단을 보호하기 위해 거짓 정보를 전달한다. -> 1-B-B
# 1-A-A | 의열단 내부의 밀정 의혹 | choice
# 당신은 경찰 신분을 이용해 폭탄을 운반할 준비를 마쳤다.
# 그런데 의열단 내부에서 김재진이 일본 경찰과 몰래 접촉한다는 소문이 퍼진다.
# 만약 김재진이 밀정이라면 폭탄 운반 계획이 발각될 수도 있다.
# 하지만 확실한 증거 없이 동료를 의심하는 것도 위험하다.
# A. 김재진에게 작전 정보를 전달하지 않는다. -> 1-A-A-A
# B. 확실한 증거가 없으니 일단 지켜본다. -> 1-A-A-B
# 1-A-B | 밀수꾼이 체포되다 | choice
# 당신은 밀수꾼에게 폭탄 운반을 맡기고 경성에 남았다.
# 그러나 운반 도중 밀수꾼이 일본 경찰의 검문에 걸리고 만다.
# 폭탄 운반에 관련된 의열단원 일부까지 체포되었다는 소식이 들려온다.
# 일본 경찰은 당신에게도 사건에 관해 질문하기 시작한다.
# A. 자신과 관계없는 일이라고 주장한다. -> 1-A-B-A
# B. 경찰 신분을 이용해 체포된 의열단원들을 풀어준다. -> 1-A-B-B
# 1-B-A | 일본 경찰의 신뢰 | choice
# 당신이 전달한 정보로 의열단원 일부가 체포되었다.
# 일본 경찰 상부는 당신의 능력을 인정하고 더욱 신뢰하기 시작한다.
# 하지만 동료들이 체포되었다는 소식을 들은 당신은 마음이 흔들린다.
# 이제 일본 경찰의 신뢰를 이용해 독립운동을 도울 수도 있고, 완전히 일본 경찰의 편에 설 수도 있다.
# A. 일본 경찰의 신뢰를 이용해 독립운동을 돕는다. -> 1-B-A-A
# B. 독립운동을 포기하고 일본 경찰에 충성한다. -> 1-B-A-B
# 1-B-B | 거짓 보고가 발각되다 | prison
# 당신은 의열단을 보호하기 위해 일본 경찰에 거짓 정보를 전달했다.
# 하지만 일본 경찰은 다른 경로로 입수한 정보와 당신의 보고가 다르다는 사실을 발견한다.
# 상부는 당신을 불러 심문한다.
# "황옥! 네가 우리를 속였다는 증거가 나왔다!"
# 결국 당신은 일본 경찰을 속인 혐의로 체포되어 감옥에 갇힌다.
# 1-A-A-A | 불신으로 무너진 작전 | failure
# 당신은 김재진에게 작전 정보를 전달하지 않기로 했다.
# 하지만 김재진은 자신을 의심하는 당신에게 강하게 반발한다.
# 의열단 내부에서는 서로를 의심하는 분위기가 퍼지기 시작한다.
# 결국 내부 갈등으로 작전 준비가 지연되고, 일본 경찰의 감시까지 강화된다.
# 폭탄 운반 계획은 실행되지 못한 채 실패로 끝난다.
# 1-A-A-B | 김재진의 배신 | choice
# 당신은 확실한 증거가 없다는 이유로 김재진을 지켜보기로 했다.
# 그러나 며칠 뒤 일본 경찰이 폭탄 운반 장소를 급습한다.
# 김재진을 통해 의열단의 정보가 일본 경찰에 전달되었던 것이다.
# 당신은 현장에서 체포되어 심문실로 끌려간다.
# 일본 경찰 간부가 묻는다.
# "황옥, 경찰인 네가 어째서 의열단과 함께 있었느냐?"
# 이제 당신은 자신의 정체를 설명해야 한다.
# A. "나는 의열단에 밀정으로 잠입한 것이다!" -> 1-A-A-B-A
# B. "나는 조선의 독립을 위해 싸웠다!" -> 1-A-A-B-B
# 1-A-B-A | 누구에게도 신뢰받지 못하다 | prison
# 당신은 체포된 의열단원들과 관계가 없다고 주장했다.
# 하지만 일본 경찰은 당신이 의열단과 접촉했다는 사실을 알아낸다.
# 한편 의열단은 당신이 동료들을 버리고 혼자 살아남으려 했다고 생각한다.
# 결국 일본 경찰과 의열단 양쪽 모두의 의심을 받게 된다.
# 당신은 일본 경찰에 체포되어 감옥에 갇힌다.
# 1-A-B-B | 폭탄 운반 성공 | choice
# 당신은 경찰 신분을 이용해 체포된 의열단원들을 풀어주었다.
# 일본 경찰은 당신의 설명을 의심했지만, 같은 경찰이라는 이유로 일단 믿어 주었다.
# 풀려난 의열단원들은 폭탄을 다시 운반하기 시작한다.
# 며칠 뒤 폭탄이 무사히 경성에 도착했다는 연락이 온다.
# 이제 공격할 장소를 결정해야 한다.
# A. 일본 식민 통치의 중심인 조선총독부를 공격한다. -> 1-A-B-B-A
# B. 일본 경찰의 주요 시설을 공격한다. -> 1-A-B-B-B
# 1-A-A-B-A | 밀정이라는 주장 | record
# 당신은 일본 경찰 간부에게 자신이 의열단에 밀정으로 잠입했다고 주장한다.
# "저는 의열단의 정보를 얻기 위해 일부러 그들과 함께 행동했습니다!"
# 일본 경찰은 당신의 과거 기록을 조사하기 시작한다.
# 조건 판정: 이전에 밀정으로 활동한 기록이 있는가?
# record-yes | 밀정 이력 인정 | traitor
# 일본 경찰은 당신이 이전에 의열단의 정보를 제공했던 기록을 발견한다.
# 당신의 주장을 받아들인 상부는 당신을 석방한다.
# 당신은 일본 경찰의 신뢰를 얻었지만, 조선의 독립을 위해 싸우던 사람들에게는 배신자로 남게 된다.
# record-no | 밀정 이력 불인정 | prison
# 일본 경찰은 당신의 주장을 뒷받침할 기록을 찾지 못한다.
# "거짓말하지 마라! 네가 의열단을 도왔다는 증거는 충분하다!"
# 결국 당신은 의열단에 협력한 혐의로 감옥에 갇힌다.
# 1-A-A-B-B | 독립운동가의 결심 | prison
# 당신은 일본 경찰의 심문 앞에서도 자신의 뜻을 굽히지 않는다.
# "나는 조선의 독립을 위해 행동했다. 후회하지 않는다!"
# 일본 경찰은 당신에게 의열단의 정보를 밝히라고 강요한다.
# 하지만 당신은 끝내 동료들의 이름을 말하지 않는다.
# 결국 당신은 독립운동에 참여한 혐의로 감옥에 갇힌다.
# 1-A-B-B-A | 조선총독부 공격 | chance70
# 당신과 의열단은 조선총독부를 공격하기로 결정한다.
# 철저한 준비 끝에 폭탄을 목표 지점까지 운반하는 데 성공한다.
# 하지만 마지막 순간까지 긴장을 늦출 수 없다.
# 이제 작전의 성공 여부가 결정된다.
# 70% 폭탄 폭발 성공 / 30% 폭탄 불발
# gov-success | 조선총독부 작전 성공 | success
# 굉음과 함께 폭탄이 폭발한다. 의열단의 작전이 성공했다는 소식이 경성에 퍼진다.
# 당신과 동료들은 일본 경찰의 추적을 피해 몸을 숨긴다.
# gov-fail | 조선총독부 작전 불발 | prison
# 폭탄이 터지지 않았다!
# 일본 경찰은 현장에서 폭탄을 발견하고 주변을 수색한다.
# 당신은 탈출을 시도하지만 결국 체포되어 감옥에 갇힌다.
# 1-A-B-B-B | 일본 경찰 시설 공격 | chance70
# 당신과 의열단은 일본 경찰의 주요 시설을 공격하기로 결정한다.
# 경찰 내부 사정을 잘 아는 당신은 동료들에게 시설의 경비 상황을 알려준다.
# 의열단은 계획에 따라 폭탄을 운반하지만, 일본 경찰의 순찰이 예상보다 빨리 시작된다.
# 과연 작전은 성공할 수 있을까?
# 70% 폭탄 폭발 성공 / 30% 폭탄 불발
# police-success | 경찰 시설 작전 성공 | success
# 의열단이 설치한 폭탄이 성공적으로 폭발한다.
# 일본 경찰은 큰 혼란에 빠지고, 당신과 동료들은 그 틈을 이용해 탈출한다.
# 위험한 작전이었지만 목표를 달성했다.
# police-fail | 경찰 시설 작전 불발 | prison
# 폭탄이 작동하지 않는다.
# 순찰 중이던 일본 경찰이 수상한 움직임을 발견하고 경보를 울린다.
# 당신은 도망치려 하지만 경찰에게 붙잡혀 감옥에 갇힌다.
# 1-B-A-A | 위험한 이중첩자 | chance60
# 당신은 일본 경찰의 신뢰를 얻은 뒤 다시 의열단을 돕기로 결심한다.
# 그러나 의열단은 이미 당신이 정보를 넘겨 동료들이 체포되었다는 사실을 알고 있다.
# 김시현이 차가운 표정으로 묻는다.
# "황옥, 우리가 당신을 다시 믿어도 되겠소?"
# 당신은 자신의 행동을 후회하며 다시 기회를 달라고 부탁한다.
# 60% 신뢰 회복 / 40% 신뢰 회복 실패
# trust-yes | 신뢰 회복 | goto
# 의열단은 당신에게 마지막 기회를 준다.
# 당신은 다시 의열단에 합류하여 폭탄 운반 작전을 준비한다.
# 1-A. 비밀 폭탄 운반 작전으로 이동합니다.
# trust-no | 신뢰 회복 실패 | exile
# 의열단은 당신의 배신을 용서하지 않는다.
# 결국 당신은 조직에서 쫓겨나고 독립운동에 다시 참여할 기회를 잃는다.
# 1-B-A-B | 배신자의 말로 | exile
# 당신은 일본 경찰에 계속 충성하기로 결정한다.
# 의열단의 정보를 넘기는 일이 반복되면서 더 많은 독립운동가가 위험에 빠진다.
# 결국 의열단은 당신이 일본 경찰의 밀정이라는 사실을 알아낸다.
# 김시현은 분노하며 말한다.
# "우리는 당신을 동지라고 믿었소. 하지만 당신은 우리를 배신했소!"
# 당신은 의열단에서 영원히 추방된다.

# --- Embedded bitmap font: Galmuri9 / SIL Open Font License ---
# Copyright (c) 2019–2025 Lee Minseo (quiple@quiple.dev)
#
# This font software is licensed under the SIL Open Font License, Version 1.1.
# This license is copied below, and is also available with a FAQ at:
# https://openfontlicense.org
#
#
# -----------------------------------------------------------
# SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
# -----------------------------------------------------------
#
# PREAMBLE
# The goals of the Open Font License (OFL) are to stimulate worldwide
# development of collaborative font projects, to support the font creation
# efforts of academic and linguistic communities, and to provide a free and
# open framework in which fonts may be shared and improved in partnership
# with others.
#
# The OFL allows the licensed fonts to be used, studied, modified and
# redistributed freely as long as they are not sold by themselves. The
# fonts, including any derivative works, can be bundled, embedded,
# redistributed and/or sold with any software provided that any reserved
# names are not used by derivative works. The fonts and derivatives,
# however, cannot be released under any other type of license. The
# requirement for fonts to remain under this license does not apply
# to any document created using the fonts or their derivatives.
#
# DEFINITIONS
# "Font Software" refers to the set of files released by the Copyright
# Holder(s) under this license and clearly marked as such. This may
# include source files, build scripts and documentation.
#
# "Reserved Font Name" refers to any names specified as such after the
# copyright statement(s).
#
# "Original Version" refers to the collection of Font Software components as
# distributed by the Copyright Holder(s).
#
# "Modified Version" refers to any derivative made by adding to, deleting,
# or substituting -- in part or in whole -- any of the components of the
# Original Version, by changing formats or by porting the Font Software to a
# new environment.
#
# "Author" refers to any designer, engineer, programmer, technical
# writer or other person who contributed to the Font Software.
#
# PERMISSION & CONDITIONS
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of the Font Software, to use, study, copy, merge, embed, modify,
# redistribute, and sell modified and unmodified copies of the Font
# Software, subject to the following conditions:
#
# 1) Neither the Font Software nor any of its individual components,
# in Original or Modified Versions, may be sold by itself.
#
# 2) Original or Modified Versions of the Font Software may be bundled,
# redistributed and/or sold with any software, provided that each copy
# contains the above copyright notice and this license. These can be
# included either as stand-alone text files, human-readable headers or
# in the appropriate machine-readable metadata fields within text or
# binary files as long as those fields can be easily viewed by the user.
#
# 3) No Modified Version of the Font Software may use the Reserved Font
# Name(s) unless explicit written permission is granted by the corresponding
# Copyright Holder. This restriction only applies to the primary font name as
# presented to the users.
#
# 4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
# Software shall not be used to promote, endorse or advertise any
# Modified Version, except to acknowledge the contribution(s) of the
# Copyright Holder(s) and the Author(s) or with their explicit written
# permission.
#
# 5) The Font Software, modified or unmodified, in part or in whole,
# must be distributed entirely under this license, and must not be
# distributed under any other license. The requirement for fonts to
# remain under this license does not apply to any document created
# using the Font Software.
#
# TERMINATION
# This license becomes null and void if any of the above conditions are
# not met.
#
# DISCLAIMER
# THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
# OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
# DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
# OTHER DEALINGS IN THE FONT SOFTWARE.
