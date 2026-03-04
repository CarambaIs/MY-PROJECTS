def main():
        print("Welcome to BMI calculator.\n")
        m, h = ask() 
        bmi = m/pow(h,2) 
        print("Your BMI: ", bmi)
def ask():
    m = input("Input your body mass(kg): ").replace("kg","")
    h = input("Input your height(cm): ").replace("cm","")
    m = float(m)
    h = float(h)  /100
    return m, h 
main()


