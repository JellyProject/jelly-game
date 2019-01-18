describe("Django REST framework / React quickstart app", () => {
    const game = {
      name: "Miguel",
      version: "jelly",
      era: 1
    };
  
    before(() => {
      cy.exec("npm run dev");
      //cy.exec("npm run flush");
    });
  
    it("should be able to fill a web form", () => {
      cy.visit("/");
  
      cy
        .get('input[name="name"]')
        .type(game.name)
        .should("have.value", game.name);
  
      cy
        .get('input[name="version"]')
        .type(game.version)
        .should("have.value", game.version);
  
      cy
        .get('textarea[name="era"]')
        .type(game.era)
        .should("have.value", "" + game.era);
  
      cy.get("form").submit();
    });

    it("should be able to see the table", () => {
        cy.visit("/");
        cy.get("tr").contains(`${game.name}${game.version}${game.era}`);
    });
    // more tests here
  });