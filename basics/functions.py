#!/usr/bin/env python3

def greeting() -> str:
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Tere", "Veterinaria")
greeting("Jorge", "DevOps")


#  DTO para defnir el tipe "Human"
class HumanDto:
    name: str
    department: str

const 