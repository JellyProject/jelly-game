import React, { Component } from "react";
import axios from "axios";
import "../css/Game.css";
import Data from "./Data";
import imageUrl from "./imageUrl";

class Game extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {
        player: Data.player,
        game: Data.game
      }
    };
  }

  beginTurn = () => {
    let player = Data.player; // !!!!!!!!!!!!!!!!!!!!!!!!!
    let game;
    axios
      .get(
        "http://127.0.0.1:8000/api/v1/games/" + this.props.join_token + "/",
        {
          headers: {
            Authorization: "Token " + this.props.token
          }
        }
      )
      .then(response => {
        game = response.data.game;
        let report = "";
        for (let key in response.data.user) {
          report += "\n" + key + " : " + response.data.user[key];
        }
        console.log(report);
      })
      .catch(error => {
        let report = "";
        for (let key in error.response.data.errors) {
          report += "\n" + key + " : " + error.response.data.errors[key];
        }
        console.log(report);
      });
    this.setState({
      data: {
        player,
        game
      }
    });
  }

  getGameData = () => {
    return this.state.data;
  };

  render() {
    return (
      <MainGrid
        getGameData={this.getGameData}
        handleActionQueue={this.handleActionQueue}
      />
    );
  }
}

class MainGrid extends Component {
  constructor(props) {
    super(props);
    this.state = {
      current_tab: "Menu",
      current_action_queue: []
    };
  }
  handleActionQueue = object => {
    if (object == null) {
      if (this.state.current_action_queue.length > 0) {
        let new_state = this.state;
        new_state.current_action_queue = [];
        this.setState(new_state);
      }
    } else if (object.name && object.family) {
      let new_state = this.state;
      new_state.current_action_queue.push(
        <ActionIcon url={imageUrl[object.name]} />
      ); //ajout d'une action à la file
      this.setState(new_state);
    }
  };
  handleTabChange = tab_name => {
    let new_state = this.state;
    new_state.current_tab = tab_name;
    this.setState(new_state);
  };
  getMainState = () => {
    return this.state;
  };
  render() {
    if (this.state.current_tab === "Technologies")
      return (
        <div className="main-grid">
          <MainHeader handleTabChange={this.handleTabChange} />
          <TechGrid
            getMainState={this.getMainState}
            handleActionQueue={this.handleActionQueue}
            getGameData={this.props.getGameData}
          />
        </div>
      );
    else if (this.state.current_tab === "Menu")
      return (
        <div className="main-grid">
          <MainHeader handleTabChange={this.handleTabChange} />
          <MenuGrid
            getMainState={this.getMainState}
            handleActionQueue={this.handleActionQueue}
            getGameData={this.props.getGameData}
          />
        </div>
      );
    else if (this.state.current_tab === "Game info")
      return (
        <div className="main-grid">
          <MainHeader handleTabChange={this.handleTabChange} />
          <GameInfoPanel getGameData={this.props.getGameData} />
        </div>
      );
  }
}

class MainHeader extends Component {
  render() {
    return (
      <div className="main-header">
        <Tab text="Menu" handleTabChange={this.props.handleTabChange} />
        <Tab text="Technologies" handleTabChange={this.props.handleTabChange} />
        <Tab text="Game info" handleTabChange={this.props.handleTabChange} />
      </div>
    );
  }
}

class Tab extends Component {
  render() {
    return (
      <div
        className="tab hover"
        onClick={() => this.props.handleTabChange(this.props.text)}
      >
        {this.props.text}
      </div>
    );
  }
}

class MenuGrid extends Component {
  render() {
    return (
      <div className="menu-grid">
        <MenuDisplay getGameData={this.props.getGameData} />
        <MenuMonitor getGameData={this.props.getGameData} />
        <MenuActionSidebar
          getMainState={this.props.getMainState}
          handleActionQueue={this.props.handleActionQueue}
          getGameData={this.props.getGameData}
        />
        <MenuFooter
          handleActionQueue={this.props.handleActionQueue}
          getGameData={this.props.getGameData}
        />
      </div>
    );
  }
}

class MenuDisplay extends Component {
  render() {
    return <div className="menu-display">DISPLAY</div>;
  }
}

class MenuMonitor extends Component {
  read = obj => {
    let res = "";
    for (let key in obj) {
      res += "\n" + key + " : " + obj[key];
    }
    return res.slice(1, res.length);
  };

  render() {
    return (
      <div className="menu-monitor">
        <MenuMonitorStats
          header="Ressources"
          text={this.read(this.props.getGameData().player.resources)}
        />
        <MenuMonitorStats
          header="Scores"
          text={this.read(this.props.getGameData().player.balance)}
        />
        <MenuMonitorStats
          header="Production / Consommation"
          text={this.read(this.props.getGameData().player.production)}
        />
        <MenuMonitorStats
          header="Réserves d'hydrocarbures"
          text={this.read(this.props.getGameData().game.hydrocarbon_piles)}
        />
      </div>
    );
  }
}

class MenuMonitorStats extends Component {
  render() {
    return (
      <div className="menu-monitor-stats">
        <div className="menu-monitor-stats-header">{this.props.header}</div>
        <div className="menu-monitor-stats-body">{this.props.text}</div>
      </div>
    );
  }
}

class MenuActionSidebar extends Component {
  render() {
    return (
      <div className="menu-action-sidebar">
        <div className="menu-action-queue">
          {this.props.getMainState().current_action_queue.map(a => a)}
        </div>
        <div
          className="menu-action-clear hover"
          onClick={() => this.props.handleActionQueue(null)}
        >
          Clear
        </div>
      </div>
    );
  }
}

class MenuFooter extends Component {
  constructor(props) {
    super(props);
    this.state = { current_selection: undefined, current_era_tab: 1 };
  }
  handleFooterTabChange = era_tab_number => {
    let new_state = this.state;
    new_state.current_era_tab = era_tab_number;
    this.setState(new_state);
  };
  handleSelection = selected_action_name => {
    if (selected_action_name) {
      let new_state = this.state;
      new_state.current_selection = {
        name: selected_action_name,
        family: "actions"
      };
      this.setState(new_state);
    } else {
      this.setState({ current_selection: null });
    }
  };
  render() {
    return (
      <div className="menu-footer">
        <MenuFooterTabs handleFooterTabChange={this.handleFooterTabChange} />
        <MenuFooterActions
          handleSelection={this.handleSelection}
          handleActionQueue={this.props.handleActionQueue}
          current_era_tab={this.state.current_era_tab}
          getGameData={this.props.getGameData}
        />
        <MenuFooterInformationPanel
          current_selection={this.state.current_selection}
          handleActionQueue={this.props.handleActionQueue}
          handleSelection={this.handleSelection}
          getGameData={this.props.getGameData}
        />
      </div>
    );
  }
}

class MenuFooterTabs extends Component {
  render() {
    return (
      <div className="menu-footer-tabs">
        <FooterTab
          text="Era 1"
          handleFooterTabChange={() => this.props.handleFooterTabChange(1)}
        />
        <FooterTab
          text="Era 2"
          handleFooterTabChange={() => this.props.handleFooterTabChange(2)}
        />
        <FooterTab
          text="Era 3"
          handleFooterTabChange={() => this.props.handleFooterTabChange(3)}
        />
      </div>
    );
  }
}

class FooterTab extends Component {
  render() {
    return (
      <div
        className="tab hover"
        onClick={() => this.props.handleFooterTabChange()}
      >
        {this.props.text}
      </div>
    );
  }
}

class MenuFooterActions extends Component {
  render() {
    let nActions = 30; // Pour afficher un nombre arbitraire d'actions pendant le dev
    let actionsList = [];
    for (let action_name in Data.actions) {
      if (Data.actions[action_name].era === this.props.current_era_tab) {
        actionsList.push(
          <Action
            name={action_name}
            url={imageUrl[action_name]}
            handleSelection={this.props.handleSelection}
            handleActionQueue={this.props.handleActionQueue}
            getGameData={this.props.getGameData}
          />
        );
      }
    }
    return <div className="menu-footer-actions">{actionsList}</div>;
  }
}

class Action extends Component {
  state = {
    action_object: Data.actions[this.props.name]
  }; //temporary (while no real info to display)

  makeInfo = description => {
    let info = "";
    for (let item in description) {
      info += `\n${item} : ${description[item]}`;
    }
    return info.slice(1);
  };

  render() {
    return (
      <img
        src={this.props.url}
        className={"action-image"}
        alt=""
        onClick={() => this.props.handleSelection(this.props.name)}
      />
    );
  }
}

class ActionIcon extends Component {
  render() {
    return <img src={this.props.url} className={"action-image"} alt="" />;
  }
}

class MenuFooterInformationPanel extends Component {
  render() {
    if (this.props.current_selection) {
      return (
        <div className="menu-footer-information-panel">
          <PurchaseButton
            current_selection={this.props.current_selection}
            handleActionQueue={this.props.handleActionQueue}
            handleSelection={this.props.handleSelection}
            getGameData={this.props.getGameData}
          />
          <CancelButton
            current_selection={this.props.current_selection}
            handleSelection={this.props.handleSelection}
          />
          <InformationDisplay
            current_selection={this.props.current_selection}
            getGameData={this.props.getGameData}
          />
        </div>
      );
    } else {
      return (
        <div className="menu-footer-information-panel">
          <EndTurnButton />
          <div className="information-display">
            (make sure you are finished with your actions)
          </div>
        </div>
      );
    }
  }
}

class InformationDisplay extends Component {
  makeInfo = action_name_and_family => {
    let action_name = action_name_and_family.name;
    let action_object = Data.actions[action_name];
    let list_modifiers = [
      "money_modifier",
      "hydrocarbon_modifier",
      "food_modifier",
      "electricity_modifier",
      "pollution_modifier",
      "waste_modifier",
      "economic_modifier",
      "social_modifier",
      "environmental_modifier"
    ];
    return (
      <div>
        <h3>{action_object.name}</h3>
        <p>{action_object.description}</p>
        <p>{"cost: " + action_object.cost}</p>
        <ul>
          {list_modifiers.map(modifier => {
            if (action_object[modifier] !== 0) {
              return <li>{modifier + ": " + action_object[modifier]}</li>;
            }
          })}
        </ul>
      </div>
    );
  };
  render() {
    if (this.props.current_selection.name) {
      let description = this.makeInfo(this.props.current_selection);
      return <div className="information-display">{description}</div>;
    } //in case it is undefined
    else {
      return <div className="information-display" />;
    }
  }
}

class PurchaseButton extends Component {
  money_missing_to_purchase = action_or_tech_object => {
    if (action_or_tech_object) {
      let player_money = this.props.getGameData().player.resources.money;
      let selection_cost =
        Data[String(action_or_tech_object.family)][
          String(action_or_tech_object.name)
        ].cost;
      console.log(
        Data[String(action_or_tech_object.family)][
          String(action_or_tech_object.name)
        ].cost
      );
      return selection_cost - player_money;
    } else {
      return null;
    }
  };

  render() {
    let missing_money = this.money_missing_to_purchase(
      this.props.current_selection
    );
    if (missing_money > 0) {
      return (
        <div className="purchase-button blocked" onClick={() => {}}>
          {"Missing " + missing_money + " coins"}
        </div>
      );
    } else if (missing_money <= 0) {
      return (
        <div
          className="purchase-button hover"
          onClick={() => {
            this.props.handleActionQueue(this.props.current_selection);
            this.props.handleSelection(null);
          }}
        >
          Purchase
        </div>
      );
    } else {
      return (
        <div className="blocked purchase-button" onClick={() => {}}>
          Purchase
        </div>
      );
    }
  }
}

class CancelButton extends Component {
  render() {
    return (
      <div
        className="cancel-button hover"
        onClick={() => this.props.handleSelection(null)}
      >
        Cancel
      </div>
    );
  }
}

class EndTurnButton extends Component {
  //ne fait rien pour le moment
  render() {
    return <div className="end-turn-button hover">End turn</div>;
  }
}

class BoxHover extends Component {
  render() {
    return <div className="box hover">{this.props.text}</div>;
  }
}

//Components from technology tab

class TechGrid extends Component {
  constructor(props) {
    super(props);
    this.state = { current_selection: undefined };
  }
  handleSelection = selected_tech_name => {
    if (selected_tech_name) {
      let new_state = this.state;
      new_state.current_selection = {
        name: selected_tech_name,
        family: "technologies"
      };
      this.setState(new_state);
    } else {
      this.setState({ current_selection: null });
    }
  };
  render() {
    return (
      <div className="tech-grid">
        <TechTree
          current_selection={this.state.current_selection}
          handleSelection={this.handleSelection}
        />
        <MenuActionSidebar
          getMainState={this.props.getMainState}
          handleActionQueue={this.props.handleActionQueue}
          getGameData={this.props.getGameData}
        />
        <TechFooter
          getMainState={this.props.getMainState}
          handleActionQueue={this.props.handleActionQueue}
          getGameData={this.props.getGameData}
          current_selection={this.state.current_selection}
          handleSelection={this.handleSelection}
        />
      </div>
    );
  }
}

class TechTree extends Component {
  makeTechTree() {
    let tech_tree = [];
    for (let tech in Data.technologies) {
      tech_tree.push(
        <Tech name={tech} handleSelection={this.props.handleSelection} />
      );
    }
    return tech_tree;
  }
  render() {
    return <div className="tech-tree">{this.makeTechTree()}</div>;
  }
}

class Tech extends Component {
  render() {
    let tech_object = Data.technologies[this.props.name];
    return (
      <div
        className="tech hover"
        onClick={() => this.props.handleSelection(this.props.name)}
      >
        <h3>{tech_object.name}</h3>
        <p style={{ fontStyle: "italic" }}>
          {tech_object.parent_technology
            ? "(Requires " + tech_object.parent_technology + ")"
            : ""}
        </p>
      </div>
    );
  }
}

class TechFooter extends Component {
  render() {
    return (
      <div className="menu-footer">
        <TechFooterButtons
          current_selection={this.props.current_selection}
          handleActionQueue={this.props.handleActionQueue}
          handleSelection={this.props.handleSelection}
          getGameData={this.props.getGameData}
        />
        <TechInformationDisplay
          current_selection={this.props.current_selection}
        />
      </div>
    );
  }
}

class TechInformationDisplay extends Component {
  makeInfo = tech_name_and_family => {
    let tech_name = tech_name_and_family.name;
    let tech_object = Data.technologies[tech_name];
    let list_modifiers = [
      "money_modifier",
      "hydrocarbon_modifier",
      "food_modifier",
      "electricity_modifier",
      "pollution_modifier",
      "waste_modifier",
      "economic_modifier",
      "social_modifier",
      "environmental_modifier"
    ];
    return (
      <div>
        <h3>{tech_object.name}</h3>
        <p>{tech_object.description}</p>
        <p>{"cost: " + tech_object.cost}</p>
        <ul>
          {list_modifiers.map(modifier => {
            if (tech_object[modifier] !== 0) {
              return <li>{modifier + ": " + tech_object[modifier]}</li>;
            }
          })}
        </ul>
        <p>
          {tech_object.child_technology != null
            ? "unlocks the following technology: " + tech_object.child_tecnology
            : ""}
        </p>
        <p>
          {tech_object.child_building != null
            ? "unlocks the following building: " + tech_object.child_building
            : ""}
        </p>
      </div>
    );
  };
  render() {
    if (this.props.current_selection) {
      let info = this.makeInfo(this.props.current_selection);
      return <div className="tech-information-display">{info}</div>;
    } //in case it is undefined
    else {
      return (
        <div className="tech-information-display">
          {" "}
          Click on a technology to get its description and then purchase it!
        </div>
      );
    }
  }
}

class TechFooterButtons extends Component {
  render() {
    if (this.props.current_selection) {
      return (
        <div className="menu-footer-information-panel">
          <PurchaseButton
            current_selection={this.props.current_selection}
            handleActionQueue={this.props.handleActionQueue}
            handleSelection={this.props.handleSelection}
            getGameData={this.props.getGameData}
          />
          <CancelButton
            current_selection={this.props.current_selection}
            handleSelection={this.props.handleSelection}
          />
        </div>
      );
    } else {
      return (
        <div className="menu-footer-information-panel">
          <EndTurnButton />
          <div className="information-display">
            (make sure you are finished with your actions)
          </div>
        </div>
      );
    }
  }
}
// components from other players' stats

class GameInfoPanel extends Component {
  render() {
    return <div className="game-info-panel" />;
  }
}

export default Game;
