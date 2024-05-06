import { useState } from "react";
import "./App.css";
import Cuenta from "./components/Cuenta";

function App() {
  const cuentas = [
    "Efectivo",
    "Clientes",
    "Deudores Diversos",
    "Funcionarios y Empleados",
    "Inventario de materiales",
    "Inventario de Producto Terminado",
  ];

  const [datosCuentas, setDatosCuentas] = useState({});

  const handleInputChange = (cuenta, valor) => {
    setDatosCuentas({ ...datosCuentas, [cuenta]: valor });
  };

  return (
    <div id="presupuesto-container">
      <h2>Presupuesto Maestro</h2>
      {cuentas.map((cuenta, index) => (
        <Cuenta
          key={index}
          nombreCuenta={cuenta}
          onInputChange={handleInputChange}
        />
      ))}
      <button onClick={() => console.log(datosCuentas)}>Guardar Datos</button>
    </div>
  );
}
export default App;
