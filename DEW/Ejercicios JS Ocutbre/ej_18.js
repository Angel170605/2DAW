class Villano {
    constructor(plan) {
        this.plan = plan;
    }

    cambiarPlan(nuevoPlan) {
        this.plan = nuevoPlan;
    }
}

const joker = new Villano('Robar banco');
document.getElementById('planActual').innerText = `El plan actual de Joker es: ${joker.plan}`;

function cambiarPlan() {
    joker.cambiarPlan('Secuestrar alcalde');
    document.getElementById('planActual').innerText = `El nuevo plan de Joker es: ${joker.plan}`;
}
