#ifndef COLLEGE_FOOTBALL_H
#define COLLEGE_FOOTBALL_H

#include <string>
#include <vector>
using namespace std;

//--------------------------------------
// Player Class
//--------------------------------------
class Player {
private:
    string name;
    int number;
    string position;
    int overallRating;
    int stamina;
    int morale;

public:
    // Constructors
    Player();
    Player(string name, int number, string position, int rating);

    // Getters and Setters
    string getName() const;
    void setName(string n);

    int getNumber() const;
    void setNumber(int num);

    string getPosition() const;
    void setPosition(string pos);

    int getOverallRating() const;
    void setOverallRating(int rating);

    int getStamina() const;
    void setStamina(int s);

    int getMorale() const;
    void setMorale(int m);

    // Methods
    void train();
    void updateStatsAfterGame(int performanceScore);
    void displayInfo() const;
};

//--------------------------------------
// Team Class
//--------------------------------------
class Team {
private:
    string teamName;
    string mascot;
    vector<Player> roster;
    int wins;
    int losses;
    int rivalryIntensity;

public:
    // Constructors
    Team();
    Team(string name, string mascot);

    // Getters and Setters
    string getTeamName() const;
    void setTeamName(string name);

    int getWins() const;
    void addWin();

    int getLosses() const;
    void addLoss();

    int getRivalryIntensity() const;
    void setRivalryIntensity(int intensity);

    // Methods
    void addPlayer(const Player& p);
    void removePlayer(int number);
    void displayRoster() const;
    void updateTeamMorale();
    int calculateTeamRating() const;
};

//--------------------------------------
// Game Class
//--------------------------------------
class Game {
private:
    Team* homeTeam;
    Team* awayTeam;
    int homeScore;
    int awayScore;
    string stadium;
    bool isRivalryGame;

public:
    // Constructors
    Game(Team* home, Team* away, string stadium, bool rivalry);

    // Getters and Setters
    int getHomeScore() const;
    int getAwayScore() const;
    void setScores(int home, int away);

    // Methods
    void playGame();
    void displayResult() const;
    void updateTeamRecords();
};

//--------------------------------------
// Rivalry Class
//--------------------------------------
class Rivalry {
private:
    Team* teamA;
    Team* teamB;
    int intensityLevel;
    vector<string> history;

public:
    // Constructors
    Rivalry(Team* a, Team* b);

    // Getters and Setters
    int getIntensityLevel() const;
    void setIntensityLevel(int level);

    // Methods
    void recordMatchResult(string result);
    void adjustIntensity(int change);
    void displayHistory() const;
};

//--------------------------------------
// Season Class
//--------------------------------------
class Season {
private:
    vector<Team> teams;
    vector<Game> schedule;
    int year;

public:
    // Constructors
    Season(int y);

    // Methods
    void addTeam(const Team& t);
    void generateSchedule();
    void playSeason();
    void displayStandings() const;
};

#endif
