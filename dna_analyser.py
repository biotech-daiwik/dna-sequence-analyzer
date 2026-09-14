while True:
    sequence=input("enter your dna sequence here:-").upper()

    if all(base in "ATGC" for base in sequence):
        break

    print("you added invalid characters in the sequence")
    
choice=input("""what do you want to analyze?

             1. Nucleotide counts
             2. Sequence length
             3. GC%
             4. Everything

Enter your choice here:-""")

if choice == "1":
    print("A=", sequence.count("A"))
    print("T=", sequence.count("T"))
    print("G=", sequence.count("G"))
    print("C=", sequence.count("C"))

elif choice == "2":
    print("sequence length =", len(sequence))

elif choice == "3":
    gc_count=sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count/len(sequence))*100
    print("GC% =", gc_percentage)

elif choice == "4":
    print("A=", sequence.count("A"))
    print("T=", sequence.count("T"))
    print("G=", sequence.count("G"))
    print("C=", sequence.count("C"))

    print("sequence length =", len(sequence))

    gc_count=sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count/len(sequence))*100
    print("GC% =", gc_percentage)

    
    
