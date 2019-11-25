# Longsword solo training assistant

Helps you perform some solo training drills for longsword under the
system of [Fiore dei Liberi](https://wiktenauer.com/wiki/Fiore_de%27i_Liberi)
as interpreted by the [Davenriche European Martial Arts School](https://www.swordfightingschool.com/).

Particularly, there are four drills, and they're all on the form "Computer
(i.e. instructor) tells you to perform a random action every so often".
You perform the action (or not!) and wait for the next instruction.

Works best (perhaps only?) on MacOS, since it uses the built-in 'say'
command to tell you the instructions. Targets Python 2.7, so will break
under Python 3 due to e.g. use of "print" as a statement.

The drills are (in increasing order of complexity):

* **Step drill**: Practice the DEMAS "Italian" footwork. 
* **Guard drill**: Stand in and move between the guards of the DEMAS system.
* **Cutting from guard to guard**: When transitioning between guards, perform
  the appropriate cuts.
* **Sticky game**: Play the DEMAS "Sticky" game with an imaginary opponent.
  Computer calls out the guard of the opponent and a distance between
  you. Your job is to move into the appropriate opposing guard and
  the specified distance. Best played with a large pole, or tree, to stand
  in for the opponent. For increased realism, perform guard transitions with
  cuts -- this will also lead to engaging the "opponent" occasionally.
