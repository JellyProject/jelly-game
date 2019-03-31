import React, { Component } from "react";
import "./App.css";
import Game from "./Game";
import WelcomePage from "./WelcomePage";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      page: "welcome_page",
      token: null,
      join_token: null
    };
  }

  saveToken = token => {
    this.setState({token});
  }

  saveJoinToken = join_token => {
    this.setState({join_token});
  }

  handlePageChange(page_name) {
    let new_state = this.state;
    new_state.page = page_name;
    this.setState(new_state);
  }
  render() {
    if (this.state.page === "game") {
      return <Game token={this.state.token} join_token={this.state.join_token}/>;
    } else {
      return (
        <WelcomePage handlePageChange={() => this.handlePageChange("game")} saveToken={this.saveToken} token={this.state.token} join_token={this.state.join_token}/>
      );
    }
  }
}

export default App;
