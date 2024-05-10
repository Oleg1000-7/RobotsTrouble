# Robots Trouble
2D игра в жанре run n gun на pygame про восстание машин

# Пояснительная записка
**Автор:** Кукреш Олег

**Идея:** Robots Trouble - это игра в жанре run n gun про восстание машин,
где игроку нужно зачищать локации от роботов

**Реализация:** 
при написании программы использовалась библиотека pygame.

код программы разделен на классы: 
 - main- содержит код, реализующий все остальные классы,
 - menu- как понятно из названия, отвечает за отображение меню,
 - game- сам игровой процесс,
 - button- кнопка,
 - object- игровой объект,
 - player- игрок,
 - enemy- противник и его поведение,
 - constants- все необходимые константы
   
основной цикл программы находится в main.
# ТЗ
**Структура:**
 - Окно главного меню:
     - кнопка перехода в игру,
     - кнопка перехода в меню настроек,
     - кнопка выхода.
 - Меню настроек:
     - ползунок изменения общей громкости игры,
     - ползунок изменения громкости эффектов,
     - ползунок изменения громкости музыки.
 - Игровой процесс:
     - игрок может перемещаться слева-направо, прыгать или пригибаться;
     - игрок может использовать различное оружие, стартовое или найденное в процессе игрыю Оружия можно менять;
     - поверхность, по которой перемещается игрок представляет собой холмистую землю, которую можно разрушать;
     - противники представляют собой роботов с различными функциями, старающихся нанести урон игроку, которых можно уничтожать;
     - игрок проходит уровень только в том случеа, когда доходит до безопасной зоны, которая находится на правом краю игрового поля.
     - игра содержит несколько уровней.
