var Data = {
  game: {
    id: 1,
    version: "jelly",
    creation_date: "2019-01-31T14:15:16.994000Z",
    last_save_date: "2019-01-31T14:15:16.994000Z",
    turn: 1,
    era: 1,
    current_index_pile: 0,
    players: [1],
    hydrocarbon_piles: [1, 2, 3],
    events: []
  },

  player: {
    id: 1,
    game: 1,
    profile: "John Doe",
    balance: {
      economic: 52,
      social: 49,
      environmental: 100
    },
    production: {
      money: 0,
      hydrocarbon: 1,
      food: 0,
      electricity: 0,
      pollution: 1,
      waste: 0
    },
    resources: {
      money: 30,
      hydrocarbon: 0
    }
  },

  actions: {
    factory: {
      id: 1,
      parent_technology: null,
      name: "Usine",
      slug: "usine",
      version: "jelly",
      era: 1,
      description: "Une simple usine de production.",
      cost: 5555,
      money_modifier: 2,
      hydrocarbon_modifier: -2,
      food_modifier: 0,
      electricity_modifier: 0,
      pollution_modifier: 2,
      waste_modifier: 0,
      economic_modifier: 0,
      social_modifier: 0,
      environmental_modifier: 0
    },
    chimneys: {
      id: 1,
      parent_technology: null,
      name: "Cheminée",
      slug: "cheminée",
      version: "jelly",
      era: 1,
      description: "Une simple usine de production.",
      cost: 3,
      money_modifier: 2,
      hydrocarbon_modifier: -2,
      food_modifier: 0,
      electricity_modifier: 0,
      pollution_modifier: 2,
      waste_modifier: 0,
      economic_modifier: 0,
      social_modifier: 0,
      environmental_modifier: 0
    },
    building: {
      id: 1,
      parent_technology: null,
      name: "Bâtiment",
      slug: "bâtiment",
      version: "jelly",
      era: 1,
      description: "Une simple usine de production.",
      cost: 3,
      money_modifier: 2,
      hydrocarbon_modifier: -2,
      food_modifier: 0,
      electricity_modifier: 0,
      pollution_modifier: 2,
      waste_modifier: 0,
      economic_modifier: 0,
      social_modifier: 0,
      environmental_modifier: 0
    }
  },

  technologies: {
    taylorism: {
      id: 1,
      name: "Taylorisme",
      slug: "taylorisme",
      version: "jelly",
      era: 1,
      description:
        "Travailler plus pour gagner plus. Effet spécial : +1 UM par usine possédée.",
      cost: 20,
      parent_technology: null,
      money_modifier: 0,
      hydrocarbon_modifier: 0,
      food_modifier: 0,
      electricity_modifier: 0,
      pollution_modifier: 0,
      waste_modifier: 0,
      economic_modifier: 2,
      social_modifier: -1,
      environmental_modifier: 0,
      child_technology: null,
      child_building: "usine-avancee"
    },
    chosisme: {
      id: 1,
      name: "Chosisme",
      slug: "chosisme",
      version: "jelly",
      era: 1,
      description:
        "Travailler plus pour gagner plus. Effet spécial : +1 UM par usine possédée.",
      cost: 20,
      parent_technology: null,
      money_modifier: 0,
      hydrocarbon_modifier: 0,
      food_modifier: 0,
      electricity_modifier: 0,
      pollution_modifier: 0,
      waste_modifier: 0,
      economic_modifier: 2,
      social_modifier: -1,
      environmental_modifier: 0,
      child_technology: null,
      child_building: "usine-avancee"
    },
    trucisme: {
      id: 1,
      name: "Trucisme",
      slug: "trucisme",
      version: "jelly",
      era: 1,
      description:
        "Travailler plus pour gagner plus. Effet spécial : +1 UM par usine possédée.",
      cost: 20,
      parent_technology: null,
      money_modifier: 0,
      hydrocarbon_modifier: 0,
      food_modifier: 0,
      electricity_modifier: 0,
      pollution_modifier: 0,
      waste_modifier: 0,
      economic_modifier: 2,
      social_modifier: -1,
      environmental_modifier: 0,
      child_technology: null,
      child_building: "usine-avancee"
    }
  },

  players: [
    {
      id: 1,
      game: 1,
      profile: "John Doe",
      balance: {
        economic: 52,
        social: 49,
        environmental: 100
      },
      production: {
        money: 0,
        hydrocarbon: 1,
        food: 0,
        electricity: 0,
        pollution: 1,
        waste: 0
      },
      resources: {
        money: 30,
        hydrocarbon: 0
      }
    },
    {
      id: 2,
      game: 1,
      profile: "John Goe",
      balance: {
        economic: 52,
        social: 49,
        environmental: 100
      },
      production: {
        money: 0,
        hydrocarbon: 1,
        food: 0,
        electricity: 0,
        pollution: 1,
        waste: 0
      },
      resources: {
        money: 30,
        hydrocarbon: 0
      }
    },
    {
      id: 3,
      game: 1,
      profile: "John Foe",
      balance: {
        economic: 52,
        social: 49,
        environmental: 100
      },
      production: {
        money: 0,
        hydrocarbon: 1,
        food: 0,
        electricity: 0,
        pollution: 1,
        waste: 0
      },
      resources: {
        money: 30,
        hydrocarbon: 0
      }
    }
  ]
};

export default Data;
