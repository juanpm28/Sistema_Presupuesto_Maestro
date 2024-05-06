// import React from 'react'
import { useState } from "react";
import PropTypes from "prop-types";

const Cuenta = ({ nombreCuenta, onInputChange }) => {
  const [valor, setValor] = useState(0);

  const handleInputChange = (e) => {
    const newValue = parseFloat(e.target.value);
    setValor(newValue);
    onInputChange(nombreCuenta, newValue);
  };

  return (
    <div className="cuenta-container">
      <label>{nombreCuenta}</label>
      <input
        type="number"
        className="input-cuentas"
        value={valor}
        onChange={handleInputChange}
      />
    </div>
  );
};

Cuenta.propTypes = {
  nombreCuenta: PropTypes.string.isRequired,
  onInputChange: PropTypes.func.isRequired,
};

export default Cuenta;
