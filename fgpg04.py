# Funny Gunny Phrase Generator VER4




import random

def generate_funny_phrase():
    """Generates a funny phrase by randomly selecting from provided lists."""
    starter = random.choice(["I'm", "It's"])

    if starter == "I'm":
            part_a = random.choice([
                "working like a",
                "sweating like a",
                "busier than a",
                "crazier than a",
                "hungrier than a",
                "as confused as a",
                "as lost as a",
                "trying harder than a",
                "as happy as a",
        ])
            
    else:  # starter == "It's"
            part_a = random.choice([
                "looking like a",
                "feeling like a",
                "raining like a",
                "better than a",
                "worse than a", 
                "wetter than a",
                "hotter than a",
                "colder than a",
                "sadder than a",
                "funnier than a",
        ])
        
    part_b = random.choice([
            "one-armed cat in a litter box",
            "cow peeing on a flat rock",
            "chicken with its head cut off",
            "frogs butt in deep ice",
            "mosquito in a nudist colony",
            "blind man at an orgy",
            "baby in a topless bar",
            "hooker in church",
 
        ])
    
    part_c = random.choice([
            "at the Helen Keller driving academy",
            "on a three-legged ox running backwards",
            "while getting a root canal from Stevie Wonder",
        ])
    
    return f"{starter} {part_a} {part_b} {part_c}."

def main():
            """Defines phrase components and generates/prints funny phrases."""
for _ in range(5):
            print(generate_funny_phrase())

if __name__ == "__main__":
            main()
# Funny Gunny Phrase Generator VER3

