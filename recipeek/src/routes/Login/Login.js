import React, { Component } from 'react';
import GradientButton from '../../components/GradientButton';
import styles from './Login.module.css';
import logo from '../../assets/recipeek-logo.png';

export default class SearchResults extends Component {
    render() {
        return (
          <div className={styles.wrapper}>
              <div>
                <img
                  src={logo}
                  alt={"logo"}
                  className={styles.logo}
                />
              </div>
              <div>
                  <div>
                    <input
                        className={styles.inputFields}
                        type="text"
                        placeholder={'Username'}
                        onChange={() => {alert('henlo!')}}
                    />
                  </div>
                  <div>
                    <input
                        className={styles.inputFields}
                        type="text"
                        placeholder={'Password'}
                        onChange={() => {alert('changed!')}}
                    />
                  </div>
              </div>
              <div>
                <GradientButton
                  label = {'Sign In'}
                  onClick = {() => {alert('clicked!')}}
                />
              </div>
          </div>
        );
    }
}
