import React from 'react';
import PropTypes from 'prop-types';
import styles from './Searchbar.module.css';

const Searchbar = (props) => {
    let { label, onClick, searchInput, onChange } = props;

    return (
        <div className={styles.searchbar}>
            <input
                className={styles.searchbarInputField}
                type="text"
                placeholder={label}
                value={searchInput}
                onChange={onChange}
            />
            <button onClick={btnCallback} className={styles.searchbarButton}>
                Search
            </button>
        </div>
    );
};

Searchbar.propTypes = {
    label: PropTypes.string,
    onClick: PropTypes.func.isRequired,
    searchInput: PropTypes.string.isRequired,
    onChange: PropTypes.func.isRequired,
};

Searchbar.defaultProps = {
    label: 'Search',
};

let btnCallback = async () => {
    let results = await fetch('http://localhost:8000/api/test')
        .then(res => res.json())
        .then(recipes => console.log(recipes))
}
export default Searchbar;
