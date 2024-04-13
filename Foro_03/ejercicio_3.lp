animal(leon;cebra; jirafa; antilope; tigre; bufalo; cocodrilo).
habitat(animal).
carnivoros(leon;tigre;cocodrilo).
herbivoros(cebra;jirafa;antilope;bufalo).
#const habitat = 3.
%Restricciones 

1 {carnivoros(_) : habitat(animal)} 1:- herbivoros(_) != carnivoros(_).
1 {animal(tigre) : habitat(animal)} 1- habitat(animal).

1 {animal(leon) : habitat(animal)} 1 :- animal(cebra;antilope;bufalo).
1 {animal(cocodrilo) : habitat(animal)} 1 :- animal(cebra;bufalo).
1 {animal(tigre) :habitat(animal)} 1 :- animal(bufalo).


