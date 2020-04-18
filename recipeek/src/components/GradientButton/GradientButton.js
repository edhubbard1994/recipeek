import React from 'react';
import PropTypes from 'prop-types';
import styles from './GradientButton.module.css';

const GradientButton = (props) => {
    let { label, onClick } = props;

    return (
        <button onClick={onClick} className={gradientbutton}>
            <p> {label} </p>
        </button>
    );
};

SecondaryButton.propTypes = {
    label: PropTypes.string.isRequired,
    onClick: PropTypes.func.isRequired,
};

export default GradientButton;
