package Farming_new;

import javafx.geometry.Pos;
import main.Node;
import main.main;
import org.osbot.rs07.api.map.Area;
import org.osbot.rs07.api.map.Position;
import org.osbot.rs07.api.model.RS2Object;
import org.osbot.rs07.event.WalkingEvent;
import org.osbot.rs07.script.MethodProvider;
import org.osbot.rs07.utility.ConditionalSleep;

import java.awt.*;
import java.io.FileNotFoundException;

public class Bank extends Node {

    Position BankPostition = new Position(3134, 3629, 0);
    Area town = new Area(3123, 3639, 3154, 3617);
    boolean getCash = false;

    public Bank(main m) {
        super(m);
    }

    @Override
    public boolean validate() {
        return (((m.getInventory().isFull() || m.getInventory().getAmount(i -> i.getName().equals("Trout") && !i.isNote()) <= 1) ||
                town.contains(m.myPosition())) && !m.isTimeToBuy() && !m.isTimeToMule() && (!m.getStarterCash()/* && m.getTimeToBank()*/)) || m.getTimeToBank();
    }

    @Override
    public int execute() throws InterruptedException{
        m.paintArea = town;
        m.log("Bank Node");
        boolean inCity = town.contains(m.myPosition());
//        m.log(inCity);
        if (!inCity) {
            m.log("Walking to bank.");
            walkToBank w = new walkToBank(m);
            if (m.myPosition().getY() > 3639) {
                w.enterFromTop();
            } else if (m.myPosition().getY() < 3617) {
                w.enterFromBottom();
            }
//            inCity = town.contains(m.myPosition());
//            m.log(inCity);

            new ConditionalSleep(3000) {
                @Override
                public boolean condition() throws InterruptedException {
                    return town.contains(m.myPosition());
                }
            }.sleep();
        }

        if (inCity && m.getBank().closest() != null && !isSetup()) {

            m.setCurrentAction("Setting up run.");

            if (m.getInventory().getAmount("Trout") <= 1  || m.getInventory().contains("Plank") || !m.getInventory().contains("Energy potion(4)")) {
                if (!m.getBank().isOpen()) {
                    m.getBank().open();
                    new ConditionalSleep(1000) {
                        @Override
                        public boolean condition() throws InterruptedException {
                            return m.getBank().isOpen();
                        }
                    }.sleep();
                }

                if (m.getBank().isOpen()) {
                    m.getBank().depositAll();

                    if (m.getInventory().getAmount("Trout") <= 1 && !m.getBank().contains("Energy potion(4)") && m.getBank().getAmount("Coins") < 100 && m.getBank().getAmount("Plank") < 50) {
                        getCash = true;
                    } else if (m.getBank().contains("Trout") && m.getBank().getAmount("Trout") > 1 &&  m.getBank().contains("Energy potion(4)")) {
                        m.getBank().withdraw("Trout", 4);
                        new ConditionalSleep(1000) {
                            @Override
                            public boolean condition() throws InterruptedException {
                                return m.getInventory().contains("Trout");
                            }
                        }.sleep();
                        m.getBank().withdraw(i -> i.getName().equals("Energy potion(4)"), 4);
                    } else if (m.getBank().isOpen() && (m.getBank().getAmount("Trout") <= 1 || !m.getBank().contains("Energy potion(4)"))) {
                        m.setTimeToBuy(true);
                        m.setTimeToBank(false);

                    }
                    new ConditionalSleep(1000) {
                        @Override
                        public boolean condition() throws InterruptedException {
                            return m.getInventory().contains("Energy potion(4)");
                        }
                    }.sleep();
                    m.getBank().close();
                }
            }
        }

        RS2Object pool = m.getObjects().closest("Pool of Refreshment");
        if (pool != null && (m.myPlayer().getHealthPercent() != 100 || m.getSettings().getRunEnergy() < 80) && (m.isTimeToBuy() || isSetup()) && inCity) {
            if (pool.getPosition().distance(m.myPosition()) > 1) {
                m.log("Walking to pool");
                m.getWalking().walk(pool.getPosition());
            }
            pool.interact();
            new ConditionalSleep(15000) {
                @Override
                public boolean condition() throws InterruptedException {
                    return m.getSettings().getRunEnergy() == 100;
                }
            }.sleep();
        }

        if (!m.isTimeToBuy() && isSetup() && inCity) {

            Position topBarrier = new Position(3134, 3639, 0);
            m.log("here");
            if (topBarrier.equals(m.myPosition()) || m.myPosition().equals(new Position(3135, 3639, 0))/*&& m.myPosition().getY() <= 3639*/) {
                m.log("passing");
                m.getCamera().moveYaw(180);
                m.getCamera().movePitch(22);
                new ConditionalSleep(2000) {
                    @Override
                    public boolean condition() throws InterruptedException {
                        return m.getCamera().getPitchAngle() == 22 && m.getCamera().getYawAngle() == 180;
                    }
                }.sleep();
                m.myPosition().hover(m.getBot());
                m.sleep(500);
                m.getMouse().click(false);
                new ConditionalSleep(3000) {
                    @Override
                    public boolean condition() throws InterruptedException {
                        return !town.contains(m.myPosition());
                    }
                }.sleep();
                m.setTimeToBank(false);
                m.setStarterCash(getCash);
                getCash = false;

            } else {
                m.log("Walking to barrier");
                WalkingEvent w = new WalkingEvent(topBarrier);
                w.setMiniMapDistanceThreshold(0);
                w.setMinDistanceThreshold(0);
                m.execute(w);
                m.log("walked");
            }
        }

        return 0;

    }


    private boolean isSetup() {
        return getCash || (m.getInventory().getAmount("Trout") > 1 && m.getInventory().contains("Energy potion(4)") && !m.getInventory().contains("Plank"));
    }
}
