#pip install pygad
import numpy as np
import pygad
import random
import time

global maxTezina
global maxVrednost

nizVrednost = []
nizTezina = []

def fitness_func(ga_instance, solution, solution_idx):
  if np.sum(solution*nizTezina) > maxTezina:
    fitness = 0
  else:
    fitness = np.sum(solution*nizVrednost)
  return fitness

def on_stop(ga_instance, solution):
  global last_fitness
  last_fitness = ga_instance.best_solution(pop_fitness = ga_instance.last_generation_fitness)[1]
  solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness) 
  print("Fitness = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
  procenat = (ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] * 100) / maxVrednost
  print("Procenat tacnosti: ", round(procenat , 2) , '%')
  print(solution)
  if ga_instance.best_solution()[1] >= maxVrednost:
    return "stop"

for i in range(1,101):
  nizVrednost.append(i)
  nizTezina.append(i)
  maxVrednost = np.sum(nizVrednost)
  maxTezina = np.sum(nizTezina)
  print("Broj clanova: ", i)  
  ga_instance = pygad.GA(
      num_generations = 100,                  #Broj generacija
      num_parents_mating = 2,                 #Broj roditelja
      fitness_func = fitness_func,            #Fitness funkcija koju smo definisali 
      sol_per_pop = 30,                       #Broj jedinki populacije
      num_genes = i,                          #Duzina jedinke 
      gene_space = [0, 1],                    #Moguci geni jedinke
      mutation_by_replacement = True,         #Gen se menja nasumicno generisanom vrednoscu
      gene_type = int,                        #Tip gena
      parent_selection_type = "sss",          #Nacin biranja roditelja, ovde koriscen metod stabilne selekcije, ali validan i tournament
      keep_parents = -1,                      #Koliko se roditelja zadrzava u sledecoj populaciji, -1 je podrazumevana vrednost i znaci da treba zadrzati sve roditelje               
      crossover_type = "single_point",        #Tip funkcije ukrstanja, koristi se ukrstanje u jednoj tacki tj. npr dete1 = roditelj1[0:tacka_ukrstanja] + roditelj2[tacka_ukrstanja:]    
      mutation_type = "random",               #Tip funkcije mutacije, ovde je koriscena slucajna mutacija
      mutation_probability = 0.1,             #Verovatnoca mutacije
      save_solutions = True,                  #Cuva fitness-e
      on_stop = on_stop,                      #Funkcija koja se poziva pri svakoj generaciji
      )
  pocetak = time.time()
  ga_instance.run()
  kraj = time.time()
  print("Vreme izvrsavanja: ", round(((kraj-pocetak)*1000) , 2) , "ms")
  print("------------------------------------------------------------------")

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness) 









