// Identifies the package where this Kotlin file belongs.
package com.archbee12.techvault

// Imports Room's annotation for defining a database table.
import androidx.room.Entity
// Imports Room's annotation for defining a primary key.
import androidx.room.PrimaryKey

// Represents one learning goal saved on the device.
@Entity(tableName = "learning_goals")
// Defines the properties of a learning goal.
data class LearningGoal(
    @PrimaryKey(autoGenerate = true)
    val id: Int = 0,
    val title: String,
    val skill: String,
    val description: String = "",
    val isCompleted: Boolean = false
)