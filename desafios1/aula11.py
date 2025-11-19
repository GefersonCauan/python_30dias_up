# Sistema de Gestão de Bonificação Anual
# Você vai criar um sistema que calcula o bônus anual de funcionários com base em:
# Cargo (Júnior, Pleno, Sênior, Gestor)
# Desempenho (de 0 a 100)
# Tempo de casa (em anos)
# E resultados da empresa no ano (lucro ou prejuízo)
# 🧠 Regras:
# Bônus base por cargo
# Júnior → 5% do salário
# Pleno → 10%
# Sênior → 15%
# Gestor → 20%
# Multiplicadores de desempenho
# Se desempenho > 90 → +50% de bônus
# Se desempenho entre 70 e 90 → bônus normal
# Se desempenho < 70 → -50% do bônus
# Tempo de casa
# A cada ano de empresa, adiciona +1% ao bônus (limitado a +10%)
# Resultado da empresa
# Se a empresa teve prejuízo, reduz o bônus total em 40%
# Se teve lucro, mantém normal
# Exibir tudo formatado:
# Cargo
# Desempenho
# Tempo de casa
# Situação da empresa
# Bônus final calculado

import copy
from dataclasses import dataclass
from typing import List
from enum import Enum
import random

class Cargo(Enum):
    JUNIOR = 'Junior'
    PLENO = 'Pleno'
    SENIOR = 'Senior'
    GESTOR = 'Gestor'
    @property
    def bunus_base(self):
        return {
            Cargo.JUNIOR: 0.05,
            Cargo.PLENO: 0.10,
            Cargo.SENIOR: 0.15,
            Cargo.GESTOR: 0.20,
        }[self]
    
class SituacaoEmpresa(Enum):
    LUCRO = 'Lucro'
    PREJUIZO = 'Prejuízo'
    @property
    def multiplicador(self):
        return {
            SituacaoEmpresa.LUCRO: 1.0,
            SituacaoEmpresa.PREJUIZO: 0.6,
        }[self]
    
@dataclass
class  Funcionario:
    nome: str
    cargo: Cargo
    desempenho: int # 0 a 100
    tempo_de_casa: int
    salario: float
    
    def calcular_bonus(self, sint_empresa: SituacaoEmpresa) -> float:
        bonus = self.salario * self.cargo.bunus_base
        
        # Ajuste por desempenho
        if self.desempenho > 90:
            bonus *= 1.5
        elif self.desempenho < 70:
            bonus *= 0.5
        
        # Ajuste por tempo de casa
        bonus *= (1 + min(self.tempo_de_casa, 10) * 0.01)
        
        # Ajuste por situação da empresa
        bonus *= sint_empresa.multiplicador
        
        return bonus
    
    def gerar_funcionario_aleatorio() -> 'Funcionario':
        nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva']
        cargos = list(Cargo)
        nomes = random.choice(nomes)
        cargo = random.choice(cargos)
        desempenho = random.randint(50, 100)
        tempo_de_casa = random.randint(0, 15)
        salario = random.uniform(3000, 15000)
        return Funcionario(nomes, cargo, desempenho, tempo_de_casa, salario)
    
def main():
    funcionarios: List[Funcionario] = [Funcionario.gerar_funcionario_aleatorio() for _ in range(5)]
    situacao_empresa = random.choice(list(SituacaoEmpresa))
    
    for func in funcionarios:
        bonus = func.calcular_bonus(situacao_empresa)
        print(f"Nome: {func.nome}")
        print(f"Cargo: {func.cargo.value}")
        print(f"Desempenho: {func.desempenho}")
        print(f"Tempo de casa: {func.tempo_de_casa} anos")
        print(f"Situação da empresa: {situacao_empresa.value}")
        print(f"Bônus final: R$ {bonus:.2f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
    