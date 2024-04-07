from pygame import*

window = display.set_mode((600,600))
fps = time.Clock()
game = True
while game:
    for e in event.get():
    if e.type == QUIT:
        game = False
    if e.type == KEYDOWN:
        if e.key==K_RIGHT:
            xforce = 5
        if e.key==K_LEFT:
            xforce = -5
        if e.key==K_DOWN:
            yforce = 5
        if e.key==K_UP:
            yforce = -5
      if e.type == KEYUP:
          if e.key==K_RIGHT:
              xforce = 0
          if e.key==K_LEFT:
              xforce = 0
          if e.key==K_DOWN:
              yforce = 0
          if e.key==K_UP:
              yforce = 0
    if e.type == MOUSEBUTTONDOWN:
        if e.button == 1:
            mx = e.pos[0]
            my = e.pos[1]


  display.update()


