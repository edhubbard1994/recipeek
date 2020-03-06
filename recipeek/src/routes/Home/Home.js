import React, { Component } from 'react';
import Searchbar from '../../components/Searchbar';

export default class Home extends Component {
    render() {
        return (
            <div>
                <h1>Recipeek</h1>
                <Searchbar
                  label = 'Search'
                  onClick = {() => {alert('Button Clicked')}}
                  searchInput = ''
                  onChange = { () => {alert('onChange')} }
                />
            </div>
        );
    }
}
