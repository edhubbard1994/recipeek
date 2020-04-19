import React, { Component } from 'react';
import GradientButton from '../../components/GradientButton';
import styles from './SignUp.module.css';
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
                  <div className={styles.inputWrap}>
                    <input
                        className={styles.inputFields}
                        type="text"
                        placeholder={'Username'}
                        onChange={() => {alert('username!')}}
                    />
                  </div>
                  <div className={styles.inputWrap}>
                    <input
                        className={styles.inputFields}
                        type="text"
                        placeholder={'email@example.com'}
                        onChange={() => {alert('email!')}}
                    />
                  </div>
                  <div className={styles.inputWrap}>
                    <input
                        className={styles.inputFields}
                        type="text"
                        placeholder={'Password'}
                        onChange={() => {alert('password!')}}
                    />
                  </div>
                  <div className={styles.inputWrap}>
                    <input
                        className={styles.inputFields}
                        type="text"
                        placeholder={'Confirm Password'}
                        onChange={() => {alert('confirm pass!')}}
                    />
                  </div>
              </div>
              <div>
                <GradientButton
                  label = {'Sign Up'}
                  onClick = {() => {alert('clicked!')}}
                />
              </div>
          </div>
        );
    }
}
