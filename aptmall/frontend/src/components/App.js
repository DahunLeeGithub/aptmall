import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePages";
import DetailPage from "./DetailPages";
import { Routes, Route, Link, Redirect, BrowserRouter as Router} from "react-router-dom";
import PurchasePage from "./purchasePages";
import ProfilePage from "./ProfilePages";
import Practice from "./practice"

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
            <div>
                <Practice />
                <Router>
                    <div>
                        <h1>hello</h1>
                        <Routes>
                            <Route path="/" element={ <HomePage /> } />
                            <Route path="/details" element={ <DetailPage /> } />
                            <Route path="/purchases" element={ <PurchasePage /> } />
                            <Route path="/profile" element={ <ProfilePage/ > } />
                        </Routes>
                    </div>
                </Router>
            </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);