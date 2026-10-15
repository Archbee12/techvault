// Identifies the package containing this file.
package com.archbee12.techvault

// Imports Context, which gives access to Android application resources.
import android.content.Context
// Imports Room's database annotation.
import androidx.room.Database
// Imports the RoomDatabase base class.
import androidx.room.Room
// Imports the Room database builder.
import androidx.room.RoomDatabase

// Creates and provides the local TechVault database.
@Database(
    entities = [LearningGoal::class],
    version = 1,
    exportSchema = false
)

// Defines the database class that Room implements.
abstract class TechVaultDatabase : RoomDatabase() {

    // Provides access to the DAO for learning goals.
    abstract fun goalDao(): GoalDao

    // Holds shared database setup and access logic.
    companion object {

        // Stores the shared database instance; volatile helps threads see updates.
        @Volatile
        private var INSTANCE: TechVaultDatabase? = null

        // Returns one shared database instance for the app.
        fun getDatabase(context: Context): TechVaultDatabase {
            return INSTANCE ?: synchronized(this) {
                INSTANCE ?: Room.databaseBuilder(
                    context.applicationContext,
                    TechVaultDatabase::class.java,
                    "techvault_database"

                // Builds the database and stores the instance for later use.
                ).build().also { INSTANCE = it }
            }
        }
    }
}