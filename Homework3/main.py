import re
import sys


def main():
    clauseNumber = 1
    clauses = []
    with open(sys.argv[1], errors='ignore') as input_file:
        for line in input_file:
            line = line.strip()
            clauses.append(line.split())

    # So to prove we have to negate the last clause
    toProve = clauses[-1]
    clauses.pop(-1)
    for eachLiteral in range(len(toProve)):
        if '~' in toProve[eachLiteral]:
            toProve[eachLiteral] = toProve[eachLiteral][1:]
        else:
            toProve[eachLiteral] = '~' + toProve[eachLiteral]

    # print initial clasuses like in the out file
    for clauseList in clauses:
        print(str(clauseNumber) + ".", ' '.join(clauseList), "{}")
        clauseNumber += 1

    # print the negated clause
    for thing in toProve:
        clauses.append([thing])
        print(str(clauseNumber) + ".", ' '.join([thing]), "{}")
        clauseNumber += 1



    cli = 1
    while cli < clauseNumber - 1:
        clj = 0
        while clj < cli:
            result = resolve(clauses[cli], clauses[clj], clauses)
            if result is False:
                print(clauseNumber, ". ","Contradiction", ' {', cli + 1, ", ", clj + 1, '}', sep='')
                clauseNumber += 1
                print("Valid")
                sys.exit(0)
            elif result is True:
                clj += 1
                continue
            else:
                print(clauseNumber, ". ",' '.join(result), ' {', cli + 1, ", ", clj + 1, '}', sep='')
                clauseNumber += 1
                clauses.append(result)
            clj += 1
        cli += 1
    print('Not Valid')


def resolve(c1, c2, clauses):
    #we need a method to take out contradictions/complements

    complementFound = False
    for l1 in c1:
        for l2 in c2:
            if neg(l1, l2):
                #if they are complements essentially take out them from the list
                complementFound = True
                resolvedClause = [lit for lit in c1+c2 if lit != l1 and lit != l2]

                # taking them out makes the clause empty FALSE
                # or if edge case theres two complements left, TRUE
                # or if clause already exists in the list, TRUE
                # otherwise just return the resolved clause
                if len(resolvedClause) == 0:
                    return False  
                if impTrue(resolvedClause):
                    return True
                for cl in clauses:
                    if Diff(resolvedClause, cl) == []:
                        return True  
                return resolvedClause

    if not complementFound:
        return True


def neg(l1, l2):
    if l1 == ('~' + l2) or l2 == ('~' + l1):
        return True
    else:
        return False


def impTrue(resolved):
    for r1 in resolved:
        for r2 in resolved:
            if neg(r1, r2):
                return True
    return False


def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

def printFunc(cl, i1, i2):
    for c in cl:
        print()


if __name__ == "__main__":
    main()
