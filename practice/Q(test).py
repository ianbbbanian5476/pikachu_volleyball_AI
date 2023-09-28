from Gridworld import Gridworld

[['+',' ',' ','P'],    # + : 終點
 [' ','W',' ',' '],    # - : 陷阱
 [' ',' ',' ',' '],    # P : player
 [' ',' ','-',' ']]    # W : 牆壁

# 走路指令 : 'u':往上, 'd':往下, 'l':往左, 'r':往右

# 建立一場遊戲
game = Gridworld( size=4, mode='static')    # size:棋盤大小(4*4)
# 查看遊戲
game.display()
# 移動 Player
game.makeMove('u')
# 獲得 Reward
game.reward()
# 遊戲狀態 (state)
game.board.render_np()