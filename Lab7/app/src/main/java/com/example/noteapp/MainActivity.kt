package com.example.noteapp

import android.app.Activity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.ListView
import android.widget.Toast

class MainActivity : Activity() {

    private lateinit var editTextNote: EditText
    private lateinit var buttonSave: Button
    private lateinit var listViewNotes: ListView
    private val notesList = mutableListOf<String>()
    private lateinit var adapter: ArrayAdapter<String>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initializeViews()
        setupAdapter()
        setupClickListeners()
    }

    private fun initializeViews() {
        editTextNote = findViewById(R.id.editTextNote)
        buttonSave = findViewById(R.id.buttonSave)
        listViewNotes = findViewById(R.id.listViewNotes)
    }

    private fun setupAdapter() {
        adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, notesList)
        listViewNotes.adapter = adapter
    }

    private fun setupClickListeners() {
        buttonSave.setOnClickListener {
            saveNote()
        }

        listViewNotes.setOnItemLongClickListener { _, _, position, _ ->
            deleteNote(position)
            true
        }
    }

    private fun saveNote() {
        val note = editTextNote.text.toString().trim()
        if (note.isNotEmpty()) {
            notesList.add(note)
            adapter.notifyDataSetChanged()
            editTextNote.text.clear()
            Toast.makeText(this, "Заметка сохранена", Toast.LENGTH_SHORT).show()
        } else {
            Toast.makeText(this, "Введите текст заметки", Toast.LENGTH_SHORT).show()
        }
    }

    private fun deleteNote(position: Int) {
        notesList.removeAt(position)
        adapter.notifyDataSetChanged()
        Toast.makeText(this, "Заметка удалена", Toast.LENGTH_SHORT).show()
    }
}