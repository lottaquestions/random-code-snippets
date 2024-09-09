#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <ostream>
#include <vector>
class SeeAndSay{
    // The interface
    class AnimalConcept{
        public:
        virtual const char* see() const = 0;
        virtual const char* say() const = 0;
    };

    // The derived type(s)
    template<typename T>
    class AnimalModel : public AnimalConcept{
        const T* m_animal;
        public:
        AnimalModel(const T* animal) : m_animal(animal){}
        
        const char* see() const { return m_animal->see(); }
        const char* say() const { return m_animal->say(); }
    };

    // Registered animals
    std::vector<AnimalConcept*> m_animals;

    public:
    template<typename T>
    void addAnimal(T* animal){
        m_animals.push_back(new AnimalModel(animal));
    }

    void pullTheString(){
        std::size_t  index = rand() % m_animals.size();

        AnimalConcept* animal = m_animals[index];
        std::cout << "The" << animal->see() <<" says " << animal->say() << std::endl ;
    }
};