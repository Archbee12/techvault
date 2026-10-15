// Identifies the package where this Kotlin file belongs.
package com.archbee12.techvault

// This is the Android's entry point configured to launch the app
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.launch

// Defines the main Android Activity for TechVault.
class MainActivity : ComponentActivity() {
    // Opens the local database and launches the app interface.
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val goalDao = TechVaultDatabase.getDatabase(this).goalDao()

        setContent {
            MaterialTheme {
                TechVaultApp(goalDao)
            }
        }
    }
}

// This is the compose function that builds the UI.
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TechVaultApp(goalDao: GoalDao) {

    // Remembers which screen is selected and restores it when possible.
    var selectedScreen by rememberSaveable { mutableStateOf("Skills") }

    // Creates the main screen layout, including the top and bottom bars.
    Scaffold(
        topBar = {
            TopAppBar(title = { Text("TechVault") })
        },
        bottomBar = {
            NavigationBar {
                // Creates a navigation item for each screen.
                listOf("Skills", "My Goals", "Add Goal").forEach { screen ->
                    NavigationBarItem(
                        // Highlights the item representing the current screen.
                        selected = selectedScreen == screen,
                        // Changes the selected screen when the item is clicked.
                        onClick = { selectedScreen = screen },
                        // This uses simple letters as icons for the navigation items.
                        icon = { Text(
                            when (screen) {
                                "Skills" -> "S"
                                "My Goals" -> "G"
                                else -> "+"
                            }
                        ) },
                        // Displays the navigation item's name.
                        label = { Text(screen) }
                    )
                }
            }
        }
    // Receives the space remaining after the top and bottom bars.
    ) { paddingValues ->
        // Chooses which screen to display based on the current selection.
        when (selectedScreen) {
            // Displays the skills screen.
            "Skills" -> SkillsScreen(
                modifier = Modifier.padding(paddingValues),
                // Opens Add Goal when a Set goal button is tapped.
                onAddGoal = { selectedScreen = "Add Goal" }
            )

            // Displays the saved learning goals.
            "My Goals" -> MyGoalsScreen(
                goalDao = goalDao,
                modifier = Modifier.padding(paddingValues)
            )

            "Add Goal" -> AddGoalScreen(
                goalDao = goalDao,
                modifier = Modifier.padding(paddingValues),
                onSaved = { selectedScreen = "My Goals" }
            )
        }
    }
}

@Composable
fun SkillsScreen(
    modifier: Modifier = Modifier,
    onAddGoal: () -> Unit
) {
    val skills = listOf(
        "Kotlin",
        "Web Development",
        "Database",
        "Cloud Computing",
        "DevOps",
        "Mobile Development"
    )

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text("Explore Skills", style = MaterialTheme.typography.headlineSmall)
        Text("Choose a skill and create a goal to track your progress.")

        LazyColumn(
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            items(skills) { skill ->
                Card(modifier = Modifier.fillMaxWidth()) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(12.dp),
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        Text(
                            text = skill,
                            modifier = Modifier.weight(1f)
                        )
                        TextButton(onClick = onAddGoal) {
                            Text("Set goal")
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun MyGoalsScreen(
    goalDao: GoalDao,
    modifier: Modifier = Modifier
) {
    val goals by goalDao.getAllGoals().collectAsState(initial = emptyList())
    val scope = rememberCoroutineScope()

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text("My Goals", style = MaterialTheme.typography.headlineSmall)

        if (goals.isEmpty()) {
            Text("You haven't saved any goals yet. Open Add Goal to create one.")
        } else {
            LazyColumn(
                verticalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                items(goals, key = { it.id }) { goal ->
                    Card(modifier = Modifier.fillMaxWidth()) {
                        Column(
                            modifier = Modifier.padding(16.dp),
                            verticalArrangement = Arrangement.spacedBy(6.dp)
                        ) {
                            Text(
                                text = goal.title,
                                style = MaterialTheme.typography.titleMedium
                            )
                            Text("Skill: ${goal.skill}")

                            if (goal.description.isNotBlank()) {
                                Text(goal.description)
                            }

                            Text(
                                if (goal.isCompleted) "Status: Completed"
                                else "Status: In progress"
                            )

                            Row(
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {
                                TextButton(
                                    onClick = {
                                        scope.launch {
                                            goalDao.updateGoal(
                                                goal.copy(
                                                    isCompleted = !goal.isCompleted
                                                )
                                            )
                                        }
                                    }
                                ) {
                                    Text(
                                        if (goal.isCompleted) "Undo"
                                        else "Mark complete"
                                    )
                                }

                                TextButton(
                                    onClick = {
                                        scope.launch {
                                            goalDao.deleteGoal(goal)
                                        }
                                    }
                                ) {
                                    Text("Delete")
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun AddGoalScreen(
    goalDao: GoalDao,
    modifier: Modifier = Modifier,
    onSaved: () -> Unit
) {
    var title by rememberSaveable { mutableStateOf("") }
    var skill by rememberSaveable { mutableStateOf("") }
    var description by rememberSaveable { mutableStateOf("") }
    var errorMessage by remember { mutableStateOf("") }

    val scope = rememberCoroutineScope()

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text("Add a Learning Goal", style = MaterialTheme.typography.headlineSmall)

        OutlinedTextField(
            value = title,
            onValueChange = { title = it },
            label = { Text("Goal title") },
            placeholder = { Text("e.g. Build a Kotlin app") },
            modifier = Modifier.fillMaxWidth(),
            singleLine = true
        )

        OutlinedTextField(
            value = skill,
            onValueChange = { skill = it },
            label = { Text("Related skill") },
            placeholder = { Text("e.g. Kotlin") },
            modifier = Modifier.fillMaxWidth(),
            singleLine = true
        )

        OutlinedTextField(
            value = description,
            onValueChange = { description = it },
            label = { Text("Description (optional)") },
            placeholder = { Text("What do you want to accomplish?") },
            modifier = Modifier.fillMaxWidth()
        )

        if (errorMessage.isNotBlank()) {
            Text(errorMessage, color = MaterialTheme.colorScheme.error)
        }

        Button(
            onClick = {
                if (title.isBlank() || skill.isBlank()) {
                    errorMessage = "Enter both a goal title and a related skill."
                } else {
                    scope.launch {
                        goalDao.insertGoal(
                            LearningGoal(
                                title = title.trim(),
                                skill = skill.trim(),
                                description = description.trim()
                            )
                        )
                        onSaved()
                    }
                }
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Save Goal")
        }
    }
}
