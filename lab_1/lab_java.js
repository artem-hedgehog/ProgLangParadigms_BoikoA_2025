class BiquadraticSolver {
    constructor() {
        this.a = 0;
        this.b = 0;
        this.c = 0;
        this.roots = [];
        this.discriminant = 0;
    }

    getValidCoefficient(promptText) {
        let value;
        while (true) {
            value = prompt(promptText);
            if (value === null) {
                console.log("Ввод отменен");
                process.exit(0);
            }
            const num = parseFloat(value);
            if (!isNaN(num)) {
                return num;
            }
            console.log("Ошибка! Введите действительное число.");
        }
    }

    solve(a, b, c) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.roots = [];

        if (this.a === 0) {
            throw new Error("Коэффициент A не может быть равен 0");
        }

        this.discriminant = Math.pow(this.b, 2) - 4 * this.a * this.c;
        console.log(`Дискриминант D = ${this.b}² - 4*${this.a}*${this.c} = ${this.discriminant}`);

        if (this.discriminant < 0) {
            console.log("Дискриминант отрицательный. Действительных корней нет.");
            return this.roots;
        }

        const t1 = (-this.b + Math.sqrt(this.discriminant)) / (2 * this.a);
        const t2 = (-this.b - Math.sqrt(this.discriminant)) / (2 * this.a);

        console.log(`Корни для t = x²: t1 = ${t1}, t2 = ${t2}`);

        if (t1 >= 0) {
            const root1 = Math.sqrt(t1);
            const root2 = -Math.sqrt(t1);
            this.roots.push(root1, root2);
            console.log(`Из t1 = ${t1} получаем корни: x = ±${root1}`);
        }

        if (t2 >= 0 && t2 !== t1) {
            const root3 = Math.sqrt(t2);
            const root4 = -Math.sqrt(t2);
            this.roots.push(root3, root4);
            console.log(`Из t2 = ${t2} получаем корни: x = ±${root3}`);
        }

        if (this.roots.length === 0) {
            console.log("Нет действительных корней (t1 и t2 отрицательные)");
        }

        return this.roots;
    }

    main() {
        console.log("Решение биквадратного уравнения вида: Ax⁴ + Bx² + C = 0");

        const a = this.getValidCoefficient("Введите коэффициент A: ");
        const b = this.getValidCoefficient("Введите коэффициент B: ");
        const c = this.getValidCoefficient("Введите коэффициент C: ");

        try {
            const roots = this.solve(a, b, c);
            if (roots.length > 0) {
                console.log("Действительные корни уравнения: ${roots.sort((x, y) => x - y)}");
            } else {
                console.log("Уравнение не имеет действительных корней.");
            }
        } catch (error) {
            console.log(`Ошибка: ${error.message}`);
        }
    }
}

if (typeof require !== 'undefined' && require.main === module) {
    const readline = require('readline');
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    function question(prompt) {
        return new Promise((resolve) => {
            rl.question(prompt, resolve);
        });
    }

    async function mainNode() {
        console.log("Решение биквадратного уравнения вида: Ax⁴ + Bx² + C = 0");
        
        const solver = new BiquadraticSolver();
        
        function getCoefficient(prompt) {
            return new Promise(async (resolve) => {
                while (true) {
                    const input = await question(prompt);
                    const num = parseFloat(input);
                    if (!isNaN(num)) {
                        resolve(num);
                        break;
                    }
                    console.log("Ошибка! Введите действительное число.");
                }
            });
        }

        const a = await getCoefficient("Введите коэффициент A: ");
        const b = await getCoefficient("Введите коэффициент B: ");
        const c = await getCoefficient("Введите коэффициент C: ");

        try {
            const roots = solver.solve(a, b, c);
            if (roots.length > 0) {
                console.log(`Действительные корни уравнения: ${roots.sort((x, y) => x - y)}`);
            } else {
                console.log("Уравнение не имеет действительных корней.");
            }
        } catch (error) {
            console.log(`Ошибка: ${error.message}`);
        }

        rl.close();
    }

    mainNode();
}