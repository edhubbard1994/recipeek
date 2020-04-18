import React, { Component } from 'react';
import styles from './Login.module.css';
import logo from '../../assets/recipeek-logo.png';

export default class SearchResults extends Component {
    render() {
        return (
          <div className={styles.wrapper}>
            <img
              src={logo}
              alt={"logo"}
              className={styles.logo}
            />
          </div>
        );
    }
}
