import collections.abc
collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft
from mcpi import block, entity
import time
import keyboard

mc = Minecraft.create()
def F():
    time.sleep(10)
def T():
    time.sleep(1)
def P():
    time.sleep(20)
#Список читов:
keyM = 'M'#Уничтожение чанков
keyN = 'N'#Положить сервер
keyV = 'V'#Ловушка с лавой и паутиной
keyX = 'X'#Под ногами блоки
keyZ = 'Z'#Защита от ТНТ
keyR = 'R'#Телепорт

#Самая важная часть!!!!
a ='sigma'


while True:
    position = mc.player.getTilePos()
    x, y, z =  position
    #Уничтожение чанков
    if keyboard.is_pressed(keyM):
        mc.setBlocks(position.x+10,position.y+10,position.z+10,position.x-10,position.y-10,position.z-10, 0)
        mc.setBlocks(position.x+1,position.y-2,position.z+1,position.x-1,position.y-2,position.z-1, 49)
        for i in range(50):
            mc.spawnEntity(position.x, position.y-8, position.z, 5)

    #Краш
    if keyboard.is_pressed(keyN):
        mc.setBlocks(position.x+1000,position.y+25,position.z+1000,position.x-1000,position.y,position.z-1000, 1)

    #Ловушка с лавой
    if keyboard.is_pressed(keyV):
        mc.setBlocks(position.x+1,position.y-2,position.z+1,position.x-1,position.y-2,position.z-1, 49)
        mc.setBlocks(position.x+5,position.y+4,position.z+5,position.x-5,position.y-4,position.z-5, 0)
        mc.setBlocks(position.x+5,position.y-4,position.z+5,position.x-5,position.y-4,position.z-5, 10)
        mc.setBlocks(position.x+1,position.y-2,position.z+1,position.x-1,position.y-2,position.z-1, 49)

    #Под ногами блоки
    if keyboard.is_pressed(keyX):
        mc.setBlocks(position.x+10,position.y-1,position.z+10,position.x-10,position.y-1,position.z-10, 1)
    
    #Защита от ТНТ
    if keyboard.is_pressed(keyZ):
        for y in range(2):
            for z in range(1):
                mc.setBlock(position.x + 1, position.y + y, position.z+z, 49)
                mc.setBlock(position.x - 1, position.y + y, position.z+z, 49)
                mc.setBlock(position.x, position.y + y, position.z + 1, 49)
                mc.setBlock(position.x, position.y + y, position.z - 1, 49)
        mc.setBlock(position.x, position.y - 1, position.z, 49)
        mc.setBlock(position.x, position.y + 2, position.z, 49)
        mc.setBlocks(position.x,position.y,position.z, 9)
        mc.setBlocks(position.x+10,position.y+10,position.z+10, 0)
        F()

    #Телепорт
    if keyboard.is_pressed(keyR):
        mc.player.setTilePos(position.x + 30, position.y, position.z)
        P()
        
    #ТНТ, стрелы и тд
    if keyboard.is_pressed(keyG):
        mc.spawnEntity(position.x+3, position.y+3, position.z, 26)
        mc.spawnEntity(position.x, position.y+6, position.z, 10)
