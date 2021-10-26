
from stack_queue_animal_shelter import (Node,dog_animal,Queue, AnimalShelter)

def test_dog:

    shelter = AnimalShelter()

    dog1 = dog_animal("Ram")

    dog2 = dog_animal("Jo")

    dog3 = dog_animal("Li")

    dog4  = dog_animal("Miro")

    shelter.enqueue(dog1)

    shelter.enqueue(dog2)

    shelter.enqueue(dog3)

    shelter.enqueue(dog4)

    assert shelter.dog == Ram Jo Li Miro

    shelter.dequeue("dog")

    assert shelter.dog == Jo Li Miro
