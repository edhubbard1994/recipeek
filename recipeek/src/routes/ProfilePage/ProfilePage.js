import React, { Component } from 'react';
import Avatar from '../../components/Avatar';
import styles from './ProfilePage.module.css';

export default class Home extends Component {

    render() {
        return (
            <div className={styles.wrapper}>
              <div className={styles.header}>
                <div className={styles.avatar}>
                  <Avatar
                    size = '10vw'
                    alt = "test image"
                    onClick = {() => {alert('clicked')}}
                    avatarData = {{
                      imageURL: 'https://images.unsplash.com/photo-1568564321589-3e581d074f9b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80',
                      username: 'user',
                    }}
                  />
                </div>
                <div className={styles.name}>
                  User Name
                </div>
              </div>
            </div>
        );
    }
}
