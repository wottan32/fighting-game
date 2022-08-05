import pygame


class Fighter:
    def __init__(self, x, y):
        self.flipped = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attack_type = 0
        self.attacking = False
        self.health = 100

    def load_image(self, sprite_sheet, animation_steps):
        # extraer imagenes desde el spritesheet
        for animation in animation_steps:
            temp_img_list = []
            for i in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, 0,self.size,self.size)
                temp_img_list.append(temp_img)



    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # accion cdo se presiona boton
        key = pygame.key.get_pressed()

        # solo se puede ejecutar otras acciones si no esta atacando
        if self.attacking == False:

            # movimientos
            if key[pygame.K_a]:
                dx -= SPEED
            if key[pygame.K_d]:
                dx = SPEED
            # salto
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            # ataque
            if key[pygame.K_p] or key[pygame.K_k]:
                self.attack(surface, target)
                # ataques
                if key[pygame.K_p]:
                    # ataque puño
                    self.attack_type = 1
                if key[pygame.K_k]:
                    # ataque patada
                    self.attack_kick = 2

        # aplicar gravedad
        self.vel_y += GRAVITY
        dy += self.vel_y

        # asegurar que los fighters no salgan del recuadro de pantalla
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom

        # asegurar que los fighters se miren de frente uno al otro
        if target.rect.centerx > self.rect.centerx:
            self.flipped = False
        else:
            self.flipped = True

        # actualizacion de posicion de fighter
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect((self.rect.centerx - (2 * self.rect.width * self.flipped), self.rect.y,
                                      2 * self.rect.width, self.rect.height))

        # golpe efectivo sobre oponente
        if attacking_rect.colliderect(target.rect):
            target.health -= 1

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
